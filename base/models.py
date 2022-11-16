from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    
class Album(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    
    class Meta:
        ordering = ['-updated','-created']
        
class Photo(models.Model):
    Album = models.ForeignKey(Album,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    img = models.ImageField(null=True)
        

