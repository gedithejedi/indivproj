import simplejson
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from getimg.api.serializers import ImageSerializer
from getimg.views import logger

@api_view(['POST',])
@csrf_exempt
def getimg(request):
    if request.method == 'POST':
        form = ImageSerializer(request.POST, request.FILES)
        if form.is_valid():
            logger.warning('form is valid')
            image = form.save()
            response_dict = {'post': 'Image Sent!'}
            return HttpResponse(simplejson.dumps(response_dict), content_type='application/javascript')
        else:
            error = form.errors
            return Response(error)



@csrf_exempt
def gettext(request):
    if 'server_response' in request.POST:
       # username = request.POST['username']
        #email = request.POST['email']
        #password = request.POST['password']
       # user = User.objects.create_user(username, email, password)
       # logger.warning(user)
        response_dict = {}
        response_dict.update({'server_response': 'working'})
        return HttpResponse(simplejson.dumps(response_dict), content_type='application/javascript')
    else:
        return render(request, 'gettext.html', {})

def success(request):
    return HttpResponse('successfully uploaded')