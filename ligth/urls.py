from django.contrib import admin
from django.urls import path
from core import views as views_core
from gallery import views as views_gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views_core.home, name='home'),
    path('equipment/', views_core.equipment, name='equipment'),
    path('bariloche/', views_gallery.bariloche, name='bariloche'),
]
