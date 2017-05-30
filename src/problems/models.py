from datetime import date

# from django.conf import settings
from django.db import models


class Problem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=False)  # ex: "Finding Earthquake Epicenters"
    date_added = models.DateField(default=date.today, blank=True, editable=True)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True, verbose_name='date submitted')
    language = models.CharField(max_length=64, verbose_name='programming language')
    file = models.BinaryField(verbose_name='source code file')

    def __str__(self):
        return self.id
