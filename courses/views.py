from django.shortcuts import render
from django import forms
from .forms import CoursesForm
from .models import Courses

# Create your views here.
def register_course(request):
    if request.method=="POST":
        form=CoursesForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CoursesForm()
    return render(request,"courses_form.html",{"form":form})


def courses_list(request):
    courses=Courses.objects.all()
    return render(request,"courses_list.html",{"courses":courses})





