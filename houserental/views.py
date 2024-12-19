from rest_framework import viewsets
from .models import data
from  .serializers import dataSerializer


class dataViewSet(viewsets.ModelViewSet):
    queryset=data.objects.all()
    serializer_class=dataSerializer