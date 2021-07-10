from django.db import models
from django.db.models.base import Model

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=9)
    last_name=models.CharField(max_length=9)
    teaching_hours=models.PositiveSmallIntegerField()
    course_unit=models.CharField(max_length=12)


