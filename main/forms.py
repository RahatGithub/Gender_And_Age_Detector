from django import forms
from .models import TestImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = TestImage
        fields = ['image']


# class ImageUploadForm(forms.Form):
#     image = forms.ImageField(label="select an image")