from django.shortcuts import render
from .models import Project

def bariloche(request):
    projects = Project.objects.all()
    print(type(projects))
    return render(request, "gallery/bariloche.html", {'projects':projects})
