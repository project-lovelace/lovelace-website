import logging

from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View

from .models import UserProfile

logger = logging.getLogger('django.' + __name__)


class UserProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request, username):
        logger.info("Getting user profile for user {:}.".format(request.user))
        user = User.objects.get(username=request.user)
        profile = UserProfile.objects.get(user=user)
        return render(request, self.template_name, {
            'user_shown': user,
            'profile': profile,
        })
