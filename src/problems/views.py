from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Problem, Submission


def index(request):
    latest_problem_list = Problem.objects.order_by('id')
    context = {'latest_problem_list': latest_problem_list}
    return render(request, 'problems/index.html', context)


def detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    template = 'problems/problem_' + str(problem.id) + '.html'
    context = {'problem': problem}
    return render(request, template, context)
