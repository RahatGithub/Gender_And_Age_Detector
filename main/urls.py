from django.urls import path
from .views import *

urlpatterns = [
    path('', UploadImageView),
    path('upload', UploadImageView),
]
