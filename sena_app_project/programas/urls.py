from django.urls import path
from .views import ProgramaCreateView, programas

app_name = 'programas'

urlpatterns = [
    path('', programas, name='lista_programas'),
    path('crear_programa/', ProgramaCreateView.as_view(), name='crear_programa'),
]