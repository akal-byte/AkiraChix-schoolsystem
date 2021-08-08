from django.db import models
from django.db.models.fields import files


# Create your models here.
class Courses(models.Model):
    title=models.CharField(max_length=12,blank=True,null=True)
    unit_id=models.CharField(max_length=14,blank=True,null=True)
    stack=models.CharField(max_length=12,blank=True,null=True)
    marketability=models.CharField(max_length=9,blank=True,null=True)
    course_id= models.CharField(max_length=12,blank=True,null=True)   
    course_duration= models.PositiveSmallIntegerField(blank=True,null=True) 
    course_material= models.FileField(blank=True,null=True) 
    course_description=models.CharField(max_length=100,blank=True,null=True)
  



    


