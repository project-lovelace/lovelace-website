from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    display_name = models.CharField(max_length=256)

    def __str__(self):
        return '{} ({})'.format(self.display_name, self.user.username)
