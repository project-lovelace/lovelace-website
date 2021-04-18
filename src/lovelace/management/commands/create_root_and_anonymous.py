import sys

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from users.models import UserProfile

class Command(BaseCommand):
    help = 'Create the root (admin) and anonymous users needed for a development environment.'

    def handle(self, *args, **options):
        User = get_user_model()

        n_users = User.objects.count()
        n_profiles = UserProfile.objects.count()

        if n_users != 0 or n_profiles != 0:
            self.stdout.write(f"There are already {n_users} users and {n_profiles} profiles. Not adding root and anonymous user profiles.")
            sys.exit(0)

        dev_password = "lovelace"

        root_user = User.objects.create_user("root", password=dev_password)
        root_user.is_superuser = True
        root_user.is_staff = True
        root_user.save()

        root_id = n_users + 1
        root_profile = UserProfile.objects.create(id=root_id, user=root_user)
        root_profile.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully created user profile: ID={root_id}, username=root, password={dev_password}"))

        anon_user = User.objects.create_user("anonymous", password=dev_password)
        anon_user.is_superuser = False
        anon_user.is_staff = False
        anon_user.save()

        anon_id = n_users + 2
        anon_profile = UserProfile.objects.create(id=anon_id, user=anon_user)
        anon_profile.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully created user profile: ID={anon_id}, username=anonymous, password={dev_password}"))
