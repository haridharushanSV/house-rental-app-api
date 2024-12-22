from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import data
from .serializers import dataSerializer
from django.conf import settings
import os

class DataViewSet(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = dataSerializer

class ImageUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        if 'photo' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        file = request.FILES['photo']
        file_name = default_storage.save(f'uploads/{file.name}', ContentFile(file.read()))
        file_url = default_storage.url(file_name)

        return Response({"url": file_url}, status=status.HTTP_201_CREATED)
class ImageUploadView(APIView):
    parser_classes = [MultiPartParser]

def post(self, request, *args, **kwargs):
        if 'photo' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        file = request.FILES['photo']
        file_path = f'uploads/{file.name}'  # Save file path relative to MEDIA_ROOT
        full_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
        
        # Make sure the directory exists
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

        with open(full_file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # Return the relative file path in the response
        return Response({"url": f"/media/{file_path}"}, status=status.HTTP_201_CREATED)