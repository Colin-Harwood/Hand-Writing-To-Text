from django.shortcuts import render

# Create your views here.
# api/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageUploadSerializer

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            # Here you can process the image with your machine learning model
            # For example:
            text = process_image_with_ml_model(image)
            return Response({'text': text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
