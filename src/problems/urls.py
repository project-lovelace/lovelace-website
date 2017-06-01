from django.conf.urls import url

from . import views

app_name = 'problems'
urlpatterns = [
    # ex: /problems/
    url(r'^$', views.index, name='index'),
    # ex: /problems/5/
    url(r'^(?P<problem_id>[0-9]+)/$', views.detail, name='detail'),
]
