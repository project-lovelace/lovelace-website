import os
import datetime

from datetime import date

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import UserProfile


class Problem(models.Model):
    def __str__(self):
        return self.title

    PHYSICS = 'physics'
    MATH = 'math'
    EARTH_SCIENCE = 'earth science'
    CHEMISTRY = 'chemistry'
    BIOLOGY = 'biology'
    ASTRONOMY = 'astronomy'
    ENGINEERING = 'engineering'
    COMPUTER_SCIENCE = 'computer science'

    SUBJECT_CHOICES = (
        (PHYSICS, 'Physics'),
        (MATH, 'Math'),
        (EARTH_SCIENCE, 'Earth science'),
        (CHEMISTRY, 'Chemistry'),
        (BIOLOGY, 'Biology'),
        (ASTRONOMY, 'Astronomy'),
        (ENGINEERING, 'Engineering'),
        (COMPUTER_SCIENCE, 'Computer science'),
    )

    id = models.AutoField(primary_key=True)

    # The order of the problems in the problem list/table.
    order_id = models.IntegerField(unique=False, validators=[MinValueValidator(0)], editable=True, null=True)

    # Unique name for database and urls, e.g. "earthquake-epicenters".
    name = models.CharField(unique=True, max_length=256, editable=True)

    # Human-readable name shown to user, e.g. "Finding Earthquake Epicenters".
    title = models.CharField(max_length=256, editable=True)

    subject = models.CharField(max_length=32, choices=SUBJECT_CHOICES, default=PHYSICS, editable=True)

    # Bit more specific than the subject, e.g. "climate science" or "cryptography".
    subfield = models.CharField(max_length=64, default="", editable=True)

    date_added = models.DateField(default=date.today, editable=True)

    solved_by = models.IntegerField(default=0, validators=[MinValueValidator(0)], editable=True)

    difficulty = models.IntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(15)], editable=True)

    timesink = models.IntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(15)], editable=True)

    visible = models.BooleanField(default=False)

# This is used to determine media filepaths for code files submitted via the "submit file" button.
def user_timestamped_filepath(instance, filename):
    datetime_now = datetime.datetime.now()
    year = datetime_now.strftime("%Y")
    month = datetime_now.strftime("%m")
    day = datetime_now.strftime("%d")

    base_filename, extension = os.path.splitext(filename)
    username = instance.user.user.username
    timestamp = datetime_now.strftime("%Y%m%d%H%M%S")
    user_timestamped_filename = f"{base_filename}_{username}_{timestamp}{extension}"

    return f"uploads/{year}/{month}/{day}/{user_timestamped_filename}"

class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    problem = models.ForeignKey(Problem, on_delete=models.PROTECT)
    test_cases_passed = models.IntegerField(default=0)
    test_cases_total = models.IntegerField(default=0)
    passed = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='submission date')
    language = models.CharField(max_length=256, verbose_name='programming language')
    file = models.FileField(upload_to=user_timestamped_filepath, verbose_name='source code file')
    runtime_sum = models.FloatField(default=0.0)
    max_mem_usage = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)
