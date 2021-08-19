from django.db import models

# Create your models here.
class Calendars(models.Model):
    event_name=models.CharField(max_length=9,blank=True,null=True)
    event_duration=models.TimeField(max_length=9,blank=True,null=True)
    event_agenda=models.CharField(max_length=200,blank=True,null=True)
    event_organizer=models.CharField(max_length=9,blank=True,null=True)
    event_venue=models.CharField(max_length=19,blank=True,null=True)
    event_attendees=models.CharField( max_length= 12,blank=True,null=True)
    





    