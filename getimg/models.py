from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Image(models.Model):
    img = models.ImageField(upload_to='images/')
    #name = models.CharField(default='name', max_length=50)

# def analyse_image(self, img):
#         image = Image.open(self.img),
