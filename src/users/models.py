import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.templatetags.static import static

from django_countries.fields import CountryField


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    display_name = models.CharField(max_length=40, default="")
    about = models.CharField(max_length=1000, blank=True)
    birthday = models.DateField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to='avatars', max_length=100, default=static("img/default_avatar.png"))

    def __str__(self):
        return '{} ({})'.format(self.display_name, self.user.username)
