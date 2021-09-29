# from django.test import TestCase
# from .models import Trainer


# # Create your tests here.

# class PictureDummyTest(TestCase):
#     def setUp(self):
#         self.trainer=Trainer(
#             first_name='Mary',
#             last_name='Dazani',
#             course_unit='IoT' ,
#             syllabus='frontend',
#             course_description="N/A",
#             gender='female',
#             phone_number=...)(
            
#             )

#     @override_settings(MEDIA_ROOT=tempfile.gettempdir())

#     def test_trainer_image_upload(self):
#             temp_file = tempfile.NamedTemporaryFile()
#             test_image = get_temporary_image(temp_file)
#             test_image.seek(0)
#             picture = Picture.objects.create(picture=test_image.name)
#             print ("It Worked!, ", picture.picture)
#             self.assertEqual(len(Picture.objects.all()), 1)



#     def test_full_name_contains_first_name(self):
#         self.assertIn(self.trainer.first_name,self.trainer.full_name())

#     def test_full_name_contains_last_name(self):
#          self.assertIn(self.trainer.last_name,self.trainer.full_name())   

