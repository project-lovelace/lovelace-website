import base64
import json

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
import requests

from .forms import CodeSubmissionForm
from .models import Problem

ENGINE_URL = 'http://localhost:14714/submit'
MAX_FILE_SIZE_BYTES = 65536


def index(request):
    latest_problem_list = Problem.objects.order_by('date_added')
    context = {'latest_problem_list': latest_problem_list}
    return render(request, 'problems/index.html', context)


def detail(request, problem_name):
    if request.method == 'GET':
        problem = get_object_or_404(Problem, pk=problem_name)
        template = 'problems/problem_{}.html'.format(str(problem_name))
        form = CodeSubmissionForm()
        context = {
            'problem': problem,
            'form': form
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form = CodeSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.files['file']
            if file.size > MAX_FILE_SIZE_BYTES:
                return HttpResponseBadRequest('File must be smaller than {} bytes'.format(MAX_FILE_SIZE_BYTES))
            submission_dict = {
                'problem': problem_name,
                'code': str(base64.b64encode(file.read()), 'utf-8')
            }
            engine_response = requests.post(ENGINE_URL, data=json.dumps(submission_dict), timeout=9999)
            results = json.loads(engine_response.text)
            return render(request, 'problems/results.html', {'results': results})
        else:
            return HttpResponseBadRequest('Unknown problem with the submitted file')

    else:
        return HttpResponseBadRequest('Unsupported HTTP method: {}'.format(request.method))
