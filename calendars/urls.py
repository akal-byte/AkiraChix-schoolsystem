from django.urls import path
from django.conf.urls import url
from . import views

app_name='calendars'

urlpatterns=[
    url("cal", views.CalendarView.as_view(), name='calendar'), # here
    url('calendars_list/', views.event, name='calendars_list'), 

]


