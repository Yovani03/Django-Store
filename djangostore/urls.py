"""
URL configuration for djangostore project.
# ... (comentarios de ejemplo)
"""
# djangostore/urls.py

from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # Vincula la URL raíz ('') a las URLs de la app 'home'
    path('', include('home.urls')), 
    path('admin/', admin.site.urls),
]

# Configuración para servir archivos media en modo DEBUG 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)