from django import forms
from django import forms
from django import forms
from django.db.models.base import Model
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
widget={
    "first_name":forms.TextInput(attrs={"class":"form-control"}),
    "last_name":forms.TextInput(attrs={"class":"form-control"}),
    "age":forms.NumberInput(attrs={"class":"form-control"}),
    "date_of_birth":forms.DateInput(attrs={"class":"form-control"}),
    "email":forms.EmailInput(attrs={"class":"form-control"}),
    "nationality":forms.Select(attrs={"class":"form-control"}),
    "gender":forms.Select(attrs={"class":"form-control"}),
    "language":forms.Select(attrs={"class":"form-control"}),
    # "image":forms.image(attrs={"class":"form-control"}),
}