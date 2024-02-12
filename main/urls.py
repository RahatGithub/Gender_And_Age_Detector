from django.urls import path
from .views import *

urlpatterns = [
    path('result', ResultView),
    path('upload', UploadImageView),
]
