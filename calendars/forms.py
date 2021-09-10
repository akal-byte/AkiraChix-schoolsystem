from django import forms
from django.db import models
from .models import Calendars
from django.forms import ModelForm, DateInput


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=Calendars
        fields="__all__"
        widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    def __init__(self, *args, **kwargs):
     super(EventRegistrationForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
     self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
     self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
