from django.urls import path

from . import views

app_name = 'problems'

urlpatterns = [
    # ex: /problems/
    path('', views.IndexView.as_view(), name='index'),

    # ex: /problems/earthquake-epicenters/
    path('<str:problem_name>/', views.detail, name='detail'),
]
