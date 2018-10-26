from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


from . import views

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls, name='admin'),

    # Main pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('news/', TemplateView.as_view(template_name='news.html'), name='news'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # User accounts
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Applications
    path('problems/', include('problems.urls'), name='problems'),
    path('users/', include('users.urls'), name='users'),

    # Favicon. See: http://staticfiles.productiondjango.com/blog/failproof-favicons/
    re_path(r'^favicon.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=False), name='favicon'),
]
