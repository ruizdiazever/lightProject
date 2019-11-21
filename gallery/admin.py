from django.contrib import admin

from django.contrib import admin

# Register your models here.
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') #

admin.site.register(Photo, PhotoAdmin)
