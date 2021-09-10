from django.urls import path
from .views import register_event
from django.conf.urls import url
from . import views

app_name='calendars'

urlpatterns=[
    path("register/",register_event,name="register_event"),
    url("cal", views.CalendarView.as_view(), name='calendar'), # here
    # url(r'^event/new/$', views.event, name='event_new'),
    # url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]


