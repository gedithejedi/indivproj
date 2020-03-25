from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Image(models.Model):
   # name = models.CharField(default='name', max_length=30)
    img = models.ImageField(upload_to='images/', max_length=1000)


# def analyse_image(self, img):
#         image = Image.open(self.img),
