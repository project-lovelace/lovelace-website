import logging
import pprint

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django_registration.backends.activation.views import RegistrationView

from .forms import CustomRegistrationForm
from users.models import UserProfile

logger = logging.getLogger('django.' + __name__)


class UserRegistrationView(RegistrationView):
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('django_registration_complete')
    template_name = 'django_registration/registration_form.html'

    def __init__(self, *args, **kwargs):
        super(UserRegistrationView, self).__init__(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CustomRegistrationForm(request.POST)

        if form.is_valid():
            user = self.create_inactive_user(form)
            user.refresh_from_db()  # load the profile instance created by the signal
            UserProfile.objects.create(user=user, display_name=user.username) # Set a default display name.
            return redirect('django_registration_complete')

        return render(request, self.template_name, {'form': form})


def error_404(request, exception):
        data = {}
        return render(request, 'error_404.html', data)

def error_500(request):
        data = {}
        return render(request, 'error_500.html', data)
