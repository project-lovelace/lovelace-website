import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.templatetags.static import static
from django.conf import settings
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator

from django_countries.fields import CountryField


def avatar_file_name(instance, filename):
    # We want a relative URL, not an absolute URL so I didn't use '/'.join(). Relative to MEDIA_ROOT.
    return "users/" + instance.user.username + "/" + filename


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    display_name = models.CharField(max_length=40, default="",
            validators=[MinLengthValidator(3), MaxLengthValidator(40)],
            help_text="Minimum and maximum length of 3-40 characters.")

    about = models.CharField(max_length=1000, blank=True,
            validators=[MaxLengthValidator(1000)],
            help_text="Maximum length of 1000 characters.")

    birthday = models.DateField(blank=True, null=True,
            help_text="Date format: YYYY-MM-DD.")

    country = CountryField(blank=True, null=True)

    location = models.CharField(max_length=50, blank=True,
            validators=[MaxLengthValidator(50)],
            help_text="Maximum length of 50 characters.")

    subscribe_to_emails = models.BooleanField(default=True, help_text="Subscribe to emails.")

    problems_solved = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    submissions_made = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return '{} ({})'.format(self.display_name, self.user.username)
