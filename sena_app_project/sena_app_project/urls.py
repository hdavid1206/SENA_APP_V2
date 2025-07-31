# senadigital/urls.py

from django.contrib import admin
from django.urls import path, include

# --- PASO 1: IMPORTACIONES ADICIONALES ---
from django.conf import settings
from django.conf.urls.static import static
# ----------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aprendices.urls')), 
]

# --- PASO 2: AÑADIR ESTA LÍNEA AL FINAL ---
# Esto le dice a Django que sirva los archivos de la carpeta /static/ 
# ÚNICAMENTE cuando DEBUG es True.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ----------------------------------------