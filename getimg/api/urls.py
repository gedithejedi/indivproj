from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include

from indivproj import settings
from getimg.api import views


app_name = 'getimg'
urlpatterns = [
    # ex: /polls/
    path('', views.getimg, name='getimg'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)