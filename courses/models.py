from django.db import models

# Create your models here.
class Courses(models.Model):
    title=models.CharField(max_length=12)
    unit_id=models.CharField(max_length=14)
    stack=models.CharField(max_length=12)
    marketability=models.CharField(max_length=9)
    


