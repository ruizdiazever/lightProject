from django.shortcuts import render
from .models import Photo
from .models import Ba

def bariloche(request):
    photos = Photo.objects.all()
    return render(request, "gallery/bariloche.html", {'photos':photos})

def ba(request):
    ba = Ba.objects.all()
    return render(request, "gallery/ba.html", {'ba':ba})

