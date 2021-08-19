from trainer.forms import TrainerRegistrationForm
from django.shortcuts import render
from django import forms
from .forms import TrainerRegistrationForm
from .models import Trainer




# Create your views here.
def register_trainer(request):
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST  ,request.FILES)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})

def trainers_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainers_list.html",{"trainers":trainers})


