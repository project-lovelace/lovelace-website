from django.conf.urls import url

from . import views

app_name = 'problems'

urlpatterns = [
    # ex: /problems/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # ex: /problems/earthquake-epicenters/
    url(r'^(?P<problem_name>[a-zA-Z0-9\-]+)/$', views.detail, name='detail'),
]
