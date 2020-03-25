import simplejson
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from getimg.api.serializers import ImageSerializer
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from .forms import *
import logging
from django.contrib.auth.models import User
logger = logging.getLogger(__name__)


# Create your views here.

# def image_view(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = ImageForm()
#     return render(request, 'index.html', {'form': form})


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
