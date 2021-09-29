from django.urls import path
from.views import register_trainer,trainers_list,edit_trainer,delete_trainer,trainer_profile

urlpatterns=[
    path("register/",register_trainer,name="register_trainer"),
    path("list/",trainers_list,name="trainers_list"),
    path("edit/<int:id>/",edit_trainer,name="edit_trainer"),
    path("profile/<int:id>/",trainer_profile,name="trainer_profile"),
    path("delete/<int:id>/",delete_trainer,name="delete_trainer")  

]
