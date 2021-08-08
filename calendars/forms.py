from django import forms
from django.db import models
from .models import Calendars

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=Calendars
        fields="__all__"