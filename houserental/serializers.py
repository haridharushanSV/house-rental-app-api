from rest_framework import serializers
from .models import data
class dataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = data
        fields=('photo','title','description','BHK','location','city','rent')