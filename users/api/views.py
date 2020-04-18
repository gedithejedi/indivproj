import simplejson
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST',])
def registration_view(request):

    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['post'] = "Successfully Registered!"
            token = Token.objects.get(user=account).key
            data['token'] = token
            return HttpResponse(simplejson.dumps(data), content_type='application/javascript')
        else:
            error = serializer.errors
        return Response(error)