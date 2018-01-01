from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls, name='admin'),

    # Main pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # User accounts
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Temporary pages
    path('tutorials/', TemplateView.as_view(template_name='temporary/tutorials.html'), name='tutorials'),
    path('tutorials/1', TemplateView.as_view(template_name='temporary/tutorial_1.html')),

    # Applications
    path('problems/', include('problems.urls'), name='problems'),
    path('users/', include('users.urls'), name='users'),
]
