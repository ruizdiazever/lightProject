from django.shortcuts import render
from .models import Photo
from .models import Ba
from .models import People
from .models import Industrial

# BARILOCHE
def bariloche(request):
    photos = Photo.objects.all()
    return render(request, "gallery/bariloche.html", {'photos':photos})

# BUENOS AIRES
def ba(request):
    ba = Ba.objects.all()
    return render(request, "gallery/ba.html", {'ba':ba})

# PEOPLE
def people(request):
    people = People.objects.all()
    return render(request, "gallery/people.html", {'people':people})

# INDUSTRIAL
def industrial(request):
    industrial = Industrial.objects.all()
    return render(request, "gallery/industrial.html", {'industrial':industrial})