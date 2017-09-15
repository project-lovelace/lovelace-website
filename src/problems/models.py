from datetime import date

# from django.conf import settings
from django.db import models


class Problem(models.Model):
    name = models.CharField(primary_key=True, max_length=256)  # ex: "earthquake-epicenters"
    title = models.CharField(max_length=256)  # shown to user, ex: "Finding Earthquake Epicenters"
    date_added = models.DateField(default=date.today, editable=True)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    passed = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='submission date')
    language = models.CharField(max_length=256, verbose_name='programming language')
    file = models.FileField(upload_to='uploads/%Y/%m/%d', verbose_name='source code file')

    def __str__(self):
        return self.id
