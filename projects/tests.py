from django.test import TestCase
from .models import Site
from django.contrib.auth.models import User
from users.models import Profile

# Create your tests here.
class SiteTestClass(TestCase):
    def setUp(self):
        self.user = User(username='alex')
        self.user.save()
        self.user_profile = Profile(user=self.user,site="mypic.png")
        self.site = Site(name="views",caption="my views",user=self.user_profile)
        
    def tearDown(self):
        Site.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.site,Site))
            
    def test_save_site(self):
        self.Site.save_site()
        sites=Site.objects.all()
        self.assertTrue(len(sites)>0)
        
    def test_delete_site(self):
        self.Site.save_site()
        self.Site.delete_site()
        sites=Site.objects.all()
        self.assertTrue(len(sites)==0)   