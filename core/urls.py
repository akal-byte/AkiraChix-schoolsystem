from django.urls import path
from .views import homes


urlpatterns=[
path("",homes, name="homes"),
# path("list/",student_list,name="Student_list"),
# path("edit/<int:id>/",edit_student,name="edit_student"),
# path("profile/<int:id>/",student_profile,name="student_profile"),
# path("delete/<int:id>/",delete_student,name="delete_student")  

]