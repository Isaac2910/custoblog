from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from . import forms


@login_required

def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})

# Create your views here.
# blog/views.py
def home(request):
    return render(request, 'blog/home.html')

# blog/views.py

from . import models



@login_required

def home(request):

    photos = models.Photo.objects.all()

    return render(request, 'blog/home.html', context={'photos': photos})

