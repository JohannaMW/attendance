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
    check_in = models.BooleanField(default=False)
    class_number = models.IntegerField(default=0)
    check_in_date = models.DateField(null=True, blank=True)
    check_in_counter = models.IntegerField(default=0)
    name = models.CharField(max_length=100, blank=True, null=True)