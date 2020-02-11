from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_photo = models.ImageField()
    Bio = models.CharField(max_length=40)

class Image(models.Model):
    image = models.ImageField()
    image_caption = models.TextField(max_length=40)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    likes = models.IntegerField(default=0, null=True)
    comments = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)


