from django.urls import path
from.views import register_trainer,trainers_list

urlpatterns=[
    path("register/",register_trainer,name="register_trainer"),
    path("list/",trainers_list,name="trainers_list"),
]