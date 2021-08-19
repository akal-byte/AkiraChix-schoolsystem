from django.shortcuts import render
from django import forms
from .forms import EventRegistrationForm
from .models import Calendars


# Create your views here.
def register_event(request):
    if request.method=="POST":
        form=EventRegistrationForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EventRegistrationForm()
    return render(request,"register_event.html",{"form":form})

def calendars_list(request):
    calendars=Calendars.objects.all()
    return render(request,"calendars_list.html",{"calendars":calendars})