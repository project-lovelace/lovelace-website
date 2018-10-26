import base64
import json
import logging
import pprint
import os
import requests
from urllib.parse import urljoin

from django.http import HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic, View
from django.db.models import F
from django.conf import settings

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

        logger.info("Adding list of previous submissions to context data...")

        previous_submissions = []
        if request.user.is_authenticated:
            current_user_profile = UserProfile.objects.get(user=request.user)
            previous_submissions_queryset = Submission.objects.filter(user=current_user_profile, problem__name=problem_name)
            for s in previous_submissions_queryset:
                logger.info("Found previous submission ID#{:d}".format(s.id))

                if s.runtime_sum < 1e-3:
                    runtime_sum = "{:d} μs".format(round(s.runtime_sum * 1e6))
                elif 1e-3 < s.runtime_sum < 1:
                    runtime_sum = "{:d} ms".format(round(s.runtime_sum * 1e3))
                else:
                    runtime_sum = "{:d} s".format(round(s.runtime_sum))

                max_mem_usage = "{:d} kB".format(round(s.max_mem_usage))

                previous_submissions.append({
                    'id': s.id,
                    'passed': s.passed,
                    'date': s.date,
                    'language': s.language,
                    'file': s.file,
                    'filename': s.file.name.split('/')[-1],
                    'test_cases_passed': s.test_cases_passed,
                    'test_cases_total': s.test_cases_total,
                    'runtime_sum': runtime_sum,
                    'max_mem_usage': max_mem_usage,
                    })

        context = {
            'problem': problem,
            'form': form,
            'previous_submissions': previous_submissions,
        }

        return render(request, template, context)

    @staticmethod
    def post(request, problem_name):
        problem = get_object_or_404(Problem, name=problem_name)
        form = CodeSubmissionForm(request.POST, request.FILES)

        if not form.is_valid():
            return HttpResponseBadRequest('Unknown problem with the submitted file')

        if not request.user.is_authenticated:
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

        test_cases_passed = 0
        test_cases_total = 0
        runtime_sum = 0.0
        max_mem_usage = 0.0

        for tc in results['testCaseDetails']:
            test_cases_total += 1
            if tc['passed']:
                test_cases_passed += 1
            runtime_sum += tc['processInfo']['utime']
            max_mem_usage = max(max_mem_usage, tc['processInfo']['maxrss'])

        submission = Submission(
            user=UserProfile.objects.get(user=request.user),
            problem=problem,
            passed=results['success'],
            language='Python3',
            file=file,
            test_cases_passed=test_cases_passed,
            test_cases_total=test_cases_total,
            runtime_sum=runtime_sum,
            max_mem_usage=max_mem_usage,
        )
        submission.save()
        template = 'problems/results.html'

        # Increment user's submission count by 1.
        UserProfile.objects.filter(user=request.user).update(submissions_made=F('submissions_made') + 1)

        # If successful and is user's first successful submission, increment problem's solved_by and user's problems_solved.
        if results['success']:
            current_user_profile = UserProfile.objects.get(user=request.user)
            num_previous_successful_submissions = Submission.objects.filter(user=current_user_profile, passed=True, problem__name=problem_name).count()
            logger.info("# previous successful submissions: {:}".format(num_previous_successful_submissions))
            if num_previous_successful_submissions == 1:
                logger.info("User {:} successfully solved {:}. Incrementing problem's solved_by 1 to TODO.".format(request.user, problem_name))
                Problem.objects.filter(name=problem_name).update(solved_by=F('solved_by') + 1)
                UserProfile.objects.filter(user=request.user).update(problems_solved=F('problems_solved') + 1)

        return JsonResponse({'results': results})
        # return render(request, template, {'results': results})
