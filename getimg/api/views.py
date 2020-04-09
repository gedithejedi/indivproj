import matplotlib
import numpy as np
import simplejson
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from pasta.augment import inline
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from getimg.api.serializers import ImageSerializer
from getimg.views import logger
import matplotlib.pyplot as mpimg
import matplotlib.pyplot as plt

import cv2
import tensorflow as tf

OBJECTS = [ "HP+Omen+2016+16+inch", "Logitech+M235" ]

# def prepare(filepath):
#     IMG_SIZE = 96
#     img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
#     new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
#     return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


def preprocess_image(img, side=96):
    min_side = min(img.shape[0], img.shape[1])
    img = img[:min_side, :min_side]
    img = cv2.resize(img, (side,side))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img.reshape(-1, side,side,1)

@api_view(['POST',])
@csrf_exempt
def getimg(request):
    if request.method == 'POST':
        serializer = ImageSerializer(request.POST, request.FILES)
        if serializer.is_valid():
            #logger.warning(form.img)
            data = {}
            logger.warning('form is valid')
            image = serializer.save()

            model = tf.keras.models.load_model("tsmodels/model.h5")
            logger.warning(model)
            # imagesent = "media/images/20200407_202030_zSqZ5El.jpg"

            imagesent = "media/" + str(image.img)
            img = cv2.imread(imagesent)
            #WORKS FOR NORMAL IMAGE
            logger.warning(img.shape)
            eval_images = preprocess_image(img)

            #plt.subplot(1, 2, 2)
            #plt.show(preprocess_image(img))
            logger.warning(eval_images[0])
             #img = cv2.imread(greyimg, 0)
            # cv2.imshow('name', img)
            # cv2.waitKey(0)
            logger.warning("IMPOrtANTE!!!!!!!!!!!!!!")
            logger.warning(eval_images.shape)
            #Something wrong with the sizes and the np.expand not working
            prediction = model.predict(eval_images)
            logger.warning(prediction)

            #"media/" + str(image.img)) )
            obj_name = OBJECTS[1] if np.argmax(prediction[0])==1 else OBJECTS[0]
            logger.warning(prediction[0])
            data ['post'] = "Image Sent!!"
            data ['object'] = obj_name
            return HttpResponse(simplejson.dumps(data), content_type='application/javascript')
        else:
            error = serializer.errors
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