from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username='alex')
        
        self.user_Profile = Profile(user=self.user,Post="mypic.png")
   
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.user_Profile,Profile))
            
    def test_save_user_Profile(self):
        self.user_Profile.save_Profile()
        Profiles=Profile.objects.all()
        self.assertTrue(len(Profiles)>0)