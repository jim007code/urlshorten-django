from django.db import models

# Create your models here.



class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords
   

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

