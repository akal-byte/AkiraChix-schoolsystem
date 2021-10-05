from django import forms
from django.db import models
from .models import Calendars
from django.forms import ModelForm, DateInput


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=Calendars
        fields="__all__"
        