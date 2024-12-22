from rest_framework import serializers
from .models import data
class dataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields=('photo1','photo2','photo3','photo4','photo5','title','description','BHK','location','city','rent','contact')

def validate_photo(self, value):
        if not value.content_type.startswith('image/'):
            raise serializers.ValidationError("Uploaded file must be an image.")
        return value