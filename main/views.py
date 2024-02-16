# views.py
from django.shortcuts import render
from .forms import ImageUploadForm 
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.image import load_img
from PIL import Image
import numpy as np
from .forms import ImageUploadForm
from .models import TestImage
from django.conf import settings
import os


# loads the image from image path and prepares it for testing
def get_image_features(image): # image denotes image path
    img = load_img(image, grayscale=True)  # loads the image and stores in an array
    img = img.resize((128, 128), Image.Resampling.LANCZOS)
    img = np.array(img)
    img = img.reshape(1, 128, 128, 1)
    img = img / 255.0
    return img 


def ResultView(request):
    queryset = TestImage.objects.all()
    result = [{
        'id' : q.id,
        'image' : q.image, 
        'gender' : q.gender,
        'age' : q.age 
    } for q in queryset]
    
    print(result)
    return render(request, 'history.html')



def UploadImageView(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image'] 
            instance = form.save(commit=False)
            instance.image = uploaded_image 
            instance.save() 

            image_path = f'media/uploaded_images/{uploaded_image}'
            model = load_model('PredictorModel_8076_dataset.h5')
            features = get_image_features(image_path)
            pred = model.predict(features)
            gender_dict = {0:'Male', 1:'Female'}
            gender = gender_dict[round(pred[0][0][0])]
            age = round(pred[1][0][0])
            
            id = instance.id 
            instance = TestImage.objects.get(id=id) # again declaring instance that is coming from the DB
            instance.gender = gender
            instance.age = age 
            instance.save()

            context={
                'uploaded_image' : image_path,
                'gender' : gender,
                'age' : age    
            }
            return render(request, 'result.html', context)
    else:
        form = ImageUploadForm()
        return render(request, 'upload_image.html', {'form' : form})