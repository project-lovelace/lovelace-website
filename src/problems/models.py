from datetime import date

from django.db import models

from users.models import UserProfile


class Problem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=256)  # ex: "earthquake-epicenters"
    title = models.CharField(max_length=256)  # shown to user, ex: "Finding Earthquake Epicenters"
    date_added = models.DateField(default=date.today, editable=True)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    passed = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='submission date')
    language = models.CharField(max_length=256, verbose_name='programming language')
    file = models.FileField(upload_to='uploads/%Y/%m/%d', verbose_name='source code file')

    def __str__(self):
        return str(self.id)
