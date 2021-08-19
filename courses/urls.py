from django.urls import path
from .views import register_course,courses_list

urlpatterns=[
    path("register/",register_course,name="register_course"),
    path("list/",courses_list,name="courses_list"),
]