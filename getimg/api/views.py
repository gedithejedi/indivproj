from venv import logger

import numpy as np
import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from getimg.api.serializers import ImageSerializer

import cv2
import tensorflow as tf

OBJECTS = [ "HP+Omen+2016+16+inch", "Logitech+M235" ]

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
            data = {}
            logger.warning('form is valid')
            image = serializer.save()

            model = tf.keras.models.load_model("tsmodels/model.h5")
            imagesent = "media/" + str(image.img)
            img = cv2.imread(imagesent)
            eval_images = preprocess_image(img)
            prediction = model.predict(eval_images)
            obj_name = OBJECTS[1] if np.argmax(prediction[0])==1 else OBJECTS[0]

            data ['post'] = "Image Sent!!"
            data ['object'] = obj_name
            return HttpResponse(simplejson.dumps(data), content_type='application/javascript')
        else:
            error = serializer.errors
            return Response(error)