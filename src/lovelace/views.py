import logging
import pprint

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

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
