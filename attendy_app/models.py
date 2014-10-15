import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class People(AbstractUser):
    TEACHER = 0
    STUDENT = 1
    TYPE = (
        (TEACHER, "teacher"),
        (STUDENT, "student")
    )
    user_type = models.PositiveSmallIntegerField(choices=TYPE, default=0)
    class_number = models.IntegerField(default=0)
    check_in_counter = models.IntegerField(default=0)
    name = models.CharField(max_length=100, blank=True, null=True)

class Checked_in(models.Model):
    date = models.DateField(default=datetime.date.today())
    user = models.ForeignKey(People, related_name='checked_in')