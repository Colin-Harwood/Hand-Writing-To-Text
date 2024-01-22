from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageUploadSerializer
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import logging
from django.conf import settings
from django.templatetags.static import static
import os

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info('Received data: %s', request.data)

        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            img_file = serializer.validated_data['image']
            
            # Convert the uploaded file to a PIL Image object
            # Convert the uploaded file to a PIL Image object
            img = Image.open(img_file).convert('L')  # convert image to grayscale
            print("Image", img)
            # Preprocess the image
            img = img.resize((28, 28))  # resize image to match model's expected input size
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.  # scale pixel values to [0, 1]

            # Invert the colors to match MNIST (white on black)
            img_array = 1 - img_array
            
            print("Shape of array", img_array.shape)


            # Load the model

            model_path = os.path.join(settings.BASE_DIR, 'models/V3ModelNumOnly.h5')
            print("Model Path", model_path)

            model = load_model(model_path)

            # Use the model to make a prediction
            prediction = model.predict(img_array)

            print("Prediction", prediction)
            # Get the class with the highest predicted probability
            predicted_class = np.argmax(prediction)
            print("Predicted Class", predicted_class)

            # Print the predicted class
            # Create a mapping of labels to characters
            labels = '0123456789'  # Only digits for MNIST

            # Get the character corresponding to the predicted class
            predicted_char = labels[predicted_class]
            print("Predicted Char", predicted_char)

            return Response({'number': predicted_char}, status=status.HTTP_200_OK)

        logger.error('Validation errors: %s', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
