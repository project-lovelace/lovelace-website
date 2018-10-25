import base64
import json
import logging
import pprint

import requests
from django.http import HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic, View
from django.db.models import F

from .forms import CodeSubmissionForm
from .models import Problem, Submission
from users.models import UserProfile

ENGINE_URL = 'http://localhost:14714/submit'
MAX_FILE_SIZE_BYTES = 65536

logger = logging.getLogger('django.' + __name__)


class IndexView(generic.ListView):
    template_name = 'problems/index.html'
    context_object_name = 'latest_problem_list'

    def get_queryset(self):
        """Return all problems, sorted chronologically."""
        return Problem.objects.order_by('date_added')

    def get_context_data(self, **kwargs):
        """ Add a list of problems solved by the user, if authenticated. """
        data = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            current_user_profile = UserProfile.objects.get(user=self.request.user)
            problems_solved = Submission.objects.filter(user=current_user_profile, passed=True).distinct().values_list('problem', flat=True)
            # logger.info("problems_solved by {:} = {:}".format(self.request.user, problems_solved))
            data['problems_solved'] = problems_solved

        return data


class DetailView(View):
    @staticmethod
    def get(request, problem_name):
        problem = get_object_or_404(Problem, name=problem_name)
        template = 'problems/problem_{}.html'.format(str(problem_name))
        form = CodeSubmissionForm()
        context = {
            'problem': problem,
            'form': form
        }
        return render(request, template, context)

    @staticmethod
    def post(request, problem_name):
        problem = get_object_or_404(Problem, name=problem_name)
        form = CodeSubmissionForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponseBadRequest('Unknown problem with the submitted file')

        user_logged_in = not request.user.is_anonymous
        if not user_logged_in:
            return HttpResponseBadRequest("You must be registered and logged in to submit code.")

        file = form.files['file']
        if file.size > MAX_FILE_SIZE_BYTES:
            return HttpResponseBadRequest('File must be smaller than {} bytes'.format(MAX_FILE_SIZE_BYTES))

        if request.is_ajax():
            logger.info("AJAX request received.")
        else:
            logger.info("Received request NOT AJAX.")

        logger.info("Received submission for problem={:}. Request:\n{:}"
                .format(problem_name, pprint.pformat(request.__dict__)))

        submission = {
            'problem': problem_name,
            'language': 'python3',
            'code': str(base64.b64encode(file.read()), 'utf-8')
        }

        engine_resp = requests.post(ENGINE_URL, data=json.dumps(submission), timeout=9999)
        status = engine_resp.status_code

        if status != 200:
            # logging.warning('Engine returned an error: {}'.format(engine_resp))
            return HttpResponseServerError('Code runner failed to run your program')

        results = json.loads(engine_resp.text)
        submission = Submission(
            user=UserProfile.objects.get(user=request.user) if user_logged_in else None,
            problem=problem,
            passed=results['success'],
            language='Python3',
            file=file,
        )
        submission.save()
        template = 'problems/results.html'

        # If successful and is user's first successful submission, increment problem's solved_by.
        if results['success']:
            current_user_profile = UserProfile.objects.get(user=request.user)
            num_previous_successful_submissions = Submission.objects.filter(user=current_user_profile, passed=True, problem__name=problem_name).count()
            logger.info("# previous successful submissions: {:}".format(num_previous_successful_submissions))
            if num_previous_successful_submissions == 1:
                logger.info("User {:} successfully solved {:}. Incrementing problem's solved_by 1 to TODO.".format(request.user, problem_name))
                Problem.objects.filter(name=problem_name).update(solved_by=F('solved_by')+1)

        return JsonResponse({'results': results})
        # return render(request, template, {'results': results})
