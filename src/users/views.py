import logging

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import EditUserProfileForm

logger = logging.getLogger('django.' + __name__)


class ViewUserProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request, username):
        logger.info("Getting user profile for user {:}.".format(username))

        user = User.objects.get(username=request.user.username)
        user_shown = User.objects.get(username=username)
        profile = UserProfile.objects.get(user=user_shown)

        return render(request, self.template_name, {
            'user': user,
            'user_shown': user_shown,
            'profile': profile,
        })


class EditUserProfileView(UpdateView):
    form_class = EditUserProfileForm
    template_name = 'users/editprofile.html'
    model = UserProfile

    def get_object(self):
        return get_object_or_404(UserProfile, pk=UserProfile.objects.get(user=self.request.user).pk)

    @method_decorator(login_required)
    def get(self, request):
        logger.info("User {:} is editing user profile.".format(request.user))

        user = User.objects.get(username=request.user)
        profile = UserProfile.objects.get(user=user)
        edit_user_profile_form = EditUserProfileForm(instance=profile)

        return render(request, self.template_name, {
            'user': user,
            'profile': profile,
            'form': edit_user_profile_form,
        })
