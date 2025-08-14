from django.urls import path
from . import views
from .views import ProgramaCreateView

app_name = 'programas'

urlpatterns = [
    path('programas/', views.programas, name='lista_programas'),
    
    # Nueva ruta para la página de creación de programas
    path('crear_programa/', views.ProgramaCreateView.as_view(), name='crear_programa'),
]