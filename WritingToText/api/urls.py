# api/urls.py

from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('api', ImageUploadView.as_view(), name='image_upload'),
]