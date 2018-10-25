from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# from django_countries.fields import CountryField


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    display_name = models.CharField(max_length=40)
    about = models.CharField(max_length=1000, default="")
    birthday = models.DateField()
    # country = CountryField()
    location = models.CharField(max_length=50, default="")
    avatar = models.ImageField(upload_to='avatars', max_length=100)
    languages_used = ArrayField(models.CharField(max_length=20))

    def __str__(self):
        return '{} ({})'.format(self.display_name, self.user.username)
