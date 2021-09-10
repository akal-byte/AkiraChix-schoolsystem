from django.db import models
from django.urls import reverse


# Create your models here.
class Calendars(models.Model):
    event_name=models.CharField(max_length=9,blank=True,null=True)
    start_time=models.DateTimeField(default='2021-06-08 00:00')
    event_id=models.CharField(max_length=10,default=1)
    end_time=models.DateTimeField(default='2021-06-08 00:00')
    event_agenda=models.CharField(max_length=200,blank=True,null=True)
    event_organizer=models.CharField(max_length=9,blank=True,null=True)
    event_venue=models.CharField(max_length=19,blank=True,null=True)
    event_attendees=models.CharField( max_length= 12,blank=True,null=True)
    ...
    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'



    