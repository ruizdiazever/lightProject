from django.contrib import admin
from django.urls import path
from core import views as views_core
from gallery import views as views_gallery
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views_core.home, name='home'),
    path('equipment/', views_core.equipment, name='equipment'),
    path('bariloche/', views_gallery.bariloche, name='bariloche'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)