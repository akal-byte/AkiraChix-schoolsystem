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

def edit_course(request,id):
    courses=Courses.objects.get(id=id)
    if request.method=="POST":
        form=CoursesForm(request.POST,instance=courses)
        if form.is_valid():
            form.save()
    else:
        form=CoursesForm(request.POST,instance=courses)
    return render(request,"edit_course.html",{"form":form})
    
def view_course(request,id):
    courses=Courses.objects.get(id=id)
    return render(request,"view_course.html",{"course":courses})

def delete_course(request,id):
    courses=Courses.objects.get(id=id)
    course.delete()
    return redirect("courses_list")




