from trainer.views import trainers_list
from django.urls import path
from django.urls import path
from .views  import register_student

urlpatterns=[
    path("register/",register_student,name="Register_Student"),
    # path("list/",student_list,name="Student_List"),
    # path("edit/<int:id>/",edit_student,name="edit_student"),
    # path("profile/<int:id>/",student_profile,name="student_profile"),
    # path("delete/<int:id>/",delete_student,name="delete_student")  
]