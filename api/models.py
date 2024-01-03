from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import FileExtensionValidator

# Create your models here.


class RydeUser(models.Model):
    user_profilepic = models.ImageField(upload_to='driver/profile_pic', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], default='driver/profile_pic/Upic.jpg')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length= 100, null=True)
    password = models.CharField(max_length= 100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    player_id = models.CharField(max_length=50, null=True)
    otp = models.CharField(max_length=4, null=True)


class CustomUserToken(models.Model):
    user = models.OneToOneField(RydeUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)
