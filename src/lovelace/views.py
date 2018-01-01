from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import UserRegistrationForm
from users.models import UserProfile

# logger = logging.getLogger(__name__)  # TODO enable logging


class UserRegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'

    # Display blank registration form
    def get(self, request):
        form = self.form_class(data=None)
        return render(request, self.template_name, {'form': form})

    # Process form data and register the user
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # TODO unnecessary?
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)  # TODO disallow bad passwords
            profile = UserProfile(user=user, display_name=username)
            profile.save()
            # user.groups.add('users')  # TODO create a group for normal users?
            login(request, user)
            return redirect(to='home')
        else:
            return render(request, self.template_name, {'form': form})
