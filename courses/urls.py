from django.urls import path
from .views import register_course,courses_list,edit_course,view_course,delete_course

urlpatterns=[
    path("register/",register_course,name="register_course"),
    path("list/",courses_list,name="courses_list"),
    path("edit/<int:id>/",edit_course,name="edit_course"),
    path("profile/<int:id>/",view_course,name="view_course"),
    path("delete/<int:id>/",delete_course,name="delete_course")  
]