from django.db import models
from django.db.models.fields import files

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=9,blank=True,null=True)
    last_name=models.CharField(max_length=9,blank=True,null=True)
    teaching_hours=models.PositiveSmallIntegerField(blank=True,null=True)
    course_unit=models.CharField(max_length=12,blank=True,null=True)
    salary=models.PositiveSmallIntegerField(blank=True,null=True)
    syllabus=models.CharField(max_length=105,blank=True,null=True)
    course_description=models.CharField(max_length=200,blank=True,null=True)
    # resume=models.FileField()
    # image=models.ImageField(blank=True,null=True)
    id_number=models.PositiveSmallIntegerField(blank=True,null=True)
    gender_choices=(
     ("Female","Female"),
     ("Male","Male"),
     ("Other","Other"),
    ) 
    gender=models.CharField(max_length=12,choices=gender_choices,blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)


