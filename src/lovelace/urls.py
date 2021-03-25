from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

from . import views, forms
from users.views import EditUserProfileView

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls, name='admin'),

    # Main pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('news/', TemplateView.as_view(template_name='news.html'), name='news'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # User accounts
    path('accounts/register/', views.UserRegistrationView.as_view(form_class=forms.CustomRegistrationForm), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('editprofile/', EditUserProfileView.as_view(success_url='/editprofile/'), name='editprofile'),

    # Applications
    path('problems/', include('problems.urls'), name='problems'),
    path('users/', include('users.urls'), name='users'),

    # Favicon. See: http://staticfiles.productiondjango.com/blog/failproof-favicons/
    re_path(r'^favicon.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=False), name='favicon'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
handler500 = views.error_500
