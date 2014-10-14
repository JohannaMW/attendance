from django.db import models
from django.contrib.auth.models import AbstractUser

class People(AbstractUser):
    TEACHER = 0
    STUDENT = 1
    TYPE = (
        (TEACHER, "teacher"),
        (STUDENT, "student")
    )
    user_type = models.PositiveSmallIntegerField(choices=TYPE)
    status = models.BooleanField(default=False)
    class_number = models.IntegerField()
    check_in_date = models.DateField()
    check_in_counter = models.IntegerField()
    name = models.CharField(max_length=100)