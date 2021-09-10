from django.db import models
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses 
from django.shortcuts import render


# Create your models here.

def homes(request):
    students=Student.objects.count()
    courses=Courses.objects.count()
    trainers=Trainer.objects.count()
    data={"students":students,"courses":courses,"trainers":trainers}
    return render(request,"homes.html",data)