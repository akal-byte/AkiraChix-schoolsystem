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

def edit_trainer(request,id):
    trainers=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST,instance=trainers)
        if form.is_valid():
            form.save()
    else:
            form=TrainerRegistrationForm(instance=trainers)
    return render(request,"edit_trainer.html",{"form":form})
    
def trainer_profile(request,id):
    trainers=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainers":trainers})

def delete_trainer(request,id):
    student=Student.objects.get(id=id)
    trainer.delete()
    return redirect("trainers_list")
