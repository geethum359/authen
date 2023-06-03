from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField()
    phone=models.CharField(max_length=10)
class register(models.Model):
    First_Name=models.CharField(max_length=10)
    Last_Name=models.CharField(max_length=10)
    Gender=models.CharField(max_length=10)
    Date_Of_Brith=models.DateField()
    Your_Email=models.EmailField()
    Phone_Number=models.IntegerField()
    Address=models.TextField(max_length=100)
  
# image carosel   
    
# class post(models.Model):
#     title = models.CharField(max_length=250)
#     description = models.TextField()
#     image = models.FileField(blank=True)
 
#     def __str__(self):
#         return self.title
# class PostImage(models.Model):
#     post = models.ForeignKey(post, default=None, on_delete=models.CASCADE)
#     images = models.FileField(upload_to = 'images/')
 
#     def __str__(self):
#         return self.post.title