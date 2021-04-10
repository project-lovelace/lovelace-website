from django.urls import path

from . import views

app_name = 'problems'

urlpatterns = [
    # e.g. /problems/
    path('', views.IndexView.as_view(), name='index'),

    # e.g. /problems/earthquake-epicenters/
    path('<str:problem_name>/', views.DetailView.as_view(), name='detail'),
]
