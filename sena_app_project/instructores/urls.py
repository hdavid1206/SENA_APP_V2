from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [
    path('instructores', views.lista_instructores, name='lista_instructores'),
    path('<int:instructor_id>/', views.detalle_instructor, name='detalle_instructor'),
]