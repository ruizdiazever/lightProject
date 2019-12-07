from django.contrib import admin
from django.contrib import admin
from django.contrib import admin

# Register your models here.
from .models import Photo
from .models import Ba

# BARILOCHE
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Photo, PhotoAdmin)

#BUENOS AIRES
class BaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Ba, BaAdmin)
