from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.

class Technologies(models.Model):
    title = models.CharField(max_length=20)
     
    def __str__(self):
        return self.title



class Site(models.Model):
    sitename = models.CharField(max_length=20)
    image = CloudinaryField('image')
    description = models.TextField()
    livelink =  models.URLField(max_length=200)
    dateuploaded = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=100)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    technlogies = models.ManyToManyField(Technologies, related_name='technologies')
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.sitename
    
    def get_absolute_url(self):
        return reverse('homepage')
    @classmethod
    def getSites(cls):
        allSites = cls.objects.all()
        return allSites


