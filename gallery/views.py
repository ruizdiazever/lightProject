from django.shortcuts import render
from .models import Photo

def bariloche(request):
    photos = Photo.objects.all()
    return render(request, "gallery/bariloche.html", {'photos':photos})

def ba(request):
    photos_ba = Ba.objects.all()
    return render(request, "gallery/ba.html", {'ba ':ba})

def example(request):
    return render (request, "gallery/example.html")