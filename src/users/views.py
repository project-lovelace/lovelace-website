import base64
import json

import requests
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.views import View

from .models import UserProfile


# logger = logging.getLogger(__name__)  # TODO enable logging


class UserProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request, username):
        user = User.objects.get(username=username)
        profile = UserProfile.objects.get(user=user)
        return render(request, self.template_name, {'user': user, 'profile': profile})
