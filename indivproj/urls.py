"""indivproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from getimg.views import *
from indivproj import settings
from django.urls import include, path


urlpatterns = [
    #Admin urls
    path('admin/', admin.site.urls),

    #Get image urls
    path('getimg/', include('getimg.api.urls')),

    #Rest framework urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/account/', include('users.api.urls','users_api')),

    path('polls/', include('polls.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
