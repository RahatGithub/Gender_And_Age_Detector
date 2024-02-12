from django.db import models


class TestImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploaded_images', blank=True)
    gender = models.CharField(max_length=10, blank=True, default='NA')
    age = models.IntegerField(blank=False, default=0)