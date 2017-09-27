import base64
import json

import requests
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from .forms import CodeSubmissionForm
from .models import Problem, Submission

ENGINE_URL = 'http://localhost:14714/submit'
MAX_FILE_SIZE_BYTES = 65536

# logger = logging.getLogger(__name__)


def index(request):
    latest_problem_list = Problem.objects.order_by('date_added')
    context = {'latest_problem_list': latest_problem_list}
    return render(request, 'problems/index.html', context)


def detail(request, problem_name):
    problem = get_object_or_404(Problem, pk=problem_name)

    if request.method == 'GET':
        template = 'problems/problem_{}.html'.format(str(problem_name))
        form = CodeSubmissionForm()
        context = {
            'problem': problem,
            'form': form
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form = CodeSubmissionForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponseBadRequest('Unknown problem with the submitted file')

        file = form.files['file']
        if file.size > MAX_FILE_SIZE_BYTES:
            return HttpResponseBadRequest('File must be smaller than {} bytes'.format(MAX_FILE_SIZE_BYTES))

        submission_dict = {
            'problem': problem_name,
            'language': 'python3',
            'code': str(base64.b64encode(file.read()), 'utf-8')
        }

        engine_resp = requests.post(ENGINE_URL, data=json.dumps(submission_dict), timeout=9999)
        status = engine_resp.status_code

        if status == 200:
            results = json.loads(engine_resp.text)
            submission = Submission(
                problem=problem,
                passed=results['success'],
                language='Python3',
                file=file,
            )
            submission.save()
            return render(request, 'problems/results.html', {'results': results})
        else:
            # logging.warning('Engine returned an error: {}'.format(engine_resp))
            return HttpResponseServerError('Code runner failed to run your program')

    else:
        return HttpResponseBadRequest('Unsupported HTTP method: {}'.format(request.method))
