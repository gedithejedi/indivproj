from rest_framework import serializers
from getimg.models import Image
#
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields =    ['img']

    def save(self):
        image = Image(
                    img =self.validated_data['img'],
            )
        image.save()
        return image
