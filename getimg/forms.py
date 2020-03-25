# forms.py
from django import forms
from .models import *
from django.middleware.csrf import get_token

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [ 'img']
