from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def equipment(request):
    return render(request, "core/equipment.html")
