from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=9)
    last_name=models.CharField(max_length=9)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
