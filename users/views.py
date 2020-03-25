from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html',{'form': form})
