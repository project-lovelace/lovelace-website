import logging
import pprint

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from users.models import UserProfile

# from django.contrib.auth import login
# from django.core.exceptions import ValidationError
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate


logger = logging.getLogger('django.' + __name__)

class UserRegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            UserProfile.objects.create(user=user)
            return redirect('login')
        else:
            form = CustomUserCreationForm()

        return render(request, self.template_name, {'form': form})
