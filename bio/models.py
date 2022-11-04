from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')

# Create your models here.
class Bio(models.Model):
    slackUsername = models.CharField(max_length = 200)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField(max_length=1000)