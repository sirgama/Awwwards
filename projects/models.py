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
    category = models.CharField(max_length=300, null=True, blank=True)
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


class Rating(models.Model):
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    
    def save_rating(self):
        self.save()
        
        
    @classmethod
    def get_ratings(cls,id):
        ratings = cls.objects.filter(site_id=id)
        return ratings  