from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import NullBooleanField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=9)
    last_name=models.CharField(max_length=9)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    email=models.EmailField()
    nationality_choices=(
     ("Kenyan","Kenyan"),
     ("Ugandan","Ugandaan"),
     ("Rwandese","Rwandese"),
     ("Sudanese","Sudanese"),
     ("South Sudanese","South Sudanese")
    )
    gender_choices=(
     ("Female","Female"),
     ("Male","Male"),
     ("Other","Other"),
    )
    language_choices=(
             ("English","English"),
             ("Kiswahili","Kiswahili"),
             ("French","French"),
    )
    nationality=models.CharField(max_length=30,choices=nationality_choices)
    gender=models.CharField(max_length=12,choices=gender_choices)
    language=models.CharField(max_length=14,choices=language_choices)
    image=models.ImageField(upload_to="images/",null=True,blank=True)
    idNumber=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=12)
    courses=models.CharField(max_length=25)
    health_records=models.FileField(upload_to='documents/%Y/%m/%d',null=True,blank=True)
    class_name=models.CharField(max_length=10,null=True,blank=True)
    room_number=models.IntegerField(null=True,blank=True)
    mentor_name=models.CharField(max_length=20,null=True,blank=True)
    big_sister=models.CharField(max_length=20,null=True,blank=True)
    asset_number=models.CharField(max_length=10,null=True,blank=True)
    guardian_name=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
