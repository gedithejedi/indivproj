from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import serializers
from getimg.models import Image
#
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def save(self):
        image = Image(
                   img =self.validated_data['img'],
            )
        image.save()

    # def send(self):
    #     image = Image(
    #                img =self.validated_data['img'],
    #         )
    #     image.save()
