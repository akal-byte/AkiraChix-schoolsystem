from django.urls import path
from.views import calendars_list, register_event

urlpatterns=[
    path("register/",register_event,name="register_event"),
    path("list/",calendars_list,name="calendars_list"),
]