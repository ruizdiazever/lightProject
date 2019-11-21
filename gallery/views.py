from django.shortcuts import render
from .models import Photo

def bariloche(request):
    photos = Photo.objects.all()
    print(type(photos))
    return render(request, "gallery/bariloche.html", {'photos':photos})

def example(request):
    return render (request, "gallery/example.html")