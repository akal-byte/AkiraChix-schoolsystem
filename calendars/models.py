from django.db import models

# Create your models here.
class Calendars(models.Model):
    type=models.CharField(max_length=12)
    price=models.PositiveSmallIntegerField()
    dates=models.DateField()
