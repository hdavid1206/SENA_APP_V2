from django.urls import path
from . import views
from .views import ProgramaCreateView

app_name = 'programas'

urlpatterns = [
    path('lista_programas/', views.programas, name='lista_programas'),
    path('crear_programa/', ProgramaCreateView.as_view(), name='crear_programa'),
]