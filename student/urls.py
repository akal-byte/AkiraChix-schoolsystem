from django.urls import path
from django.urls import path
from .views  import register_student 

urlpatterns=[
    path("register/",register_student,name="Register_Student"),
]