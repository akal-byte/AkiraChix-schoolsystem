from trainer.views import trainers_list
from django.urls import path
from django.urls import path
from .views  import register_student, student_list

urlpatterns=[
    path("register/",register_student,name="Register_Student"),
    path("list/",student_list,name="Student_List"),
]