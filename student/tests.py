from django import test
from django.conf.urls import url
from django.http import response
from django.test import TestCase
from .models import Student
import datetime
from django.urls import reverse
# Create your tests here.
# override a module called testcase

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(
            first_name="Mary",last_name="Owuor",age=23,
            courses="Python",
            phone_number="0723456789",
            idNumber=456790,
            email="owuormary@gmail.com",
            
            )
    
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())
        # assert takes 2 attributes

    def test_full_name_contains_last_name(self):
         self.assertIn(self.student.last_name,self.student.full_name())   


    def test_year_of_birth(self):
        year=datetime.datetime.now().year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())


    def test_student_registration_view(self):
        self.data={'first_name':self.student.first_name,
                   'last_name':self.student.last_name,
                   'age':self.student.age
        }
        url=reverse("register_student")
        response=self.client.post(url,self.data)
        self.assertEqual(response.status_code,200)     
    

    # def test_student_list(self):

    # def test_student_profile():

    # def test_edit_student();