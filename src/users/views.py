from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View

from .models import UserProfile

# logger = logging.getLogger(__name__)  # TODO enable logging


class UserProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request, username):
        user = User.objects.get(username=username)
        profile = UserProfile.objects.get(user=user)
        return render(request, self.template_name, {
            'user_shown': user,
            'profile': profile,
        })
