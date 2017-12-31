from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # Administration
    url(r'^admin/', admin.site.urls, name='admin'),

    # Main pages
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # User accounts
    url(r'^register$', views.UserRegistrationView.as_view(), name='register'),
    url(r'^login$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout$', auth_views.LogoutView.as_view(), name='logout'),

    # Temporary pages
    url(r'^tutorials/$', TemplateView.as_view(template_name='temporary/tutorials.html'), name='tutorials'),
    url(r'^tutorials/1$', TemplateView.as_view(template_name='temporary/tutorial_1.html')),

    # The problems app
    url(r'^problems/', include('problems.urls'), name='problems'),
]
