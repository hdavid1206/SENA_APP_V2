from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz
from django.shortcuts import render
from instructores.models import Instructor
# Create your views here.

def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().order_by('apellido', 'nombre')
    total_aprendices = lista_aprendices.count()
    context = {
        'lista_aprendices': lista_aprendices,
        'total_aprendices': total_aprendices,
    }
    return render(request, 'lista_aprendices.html', context)

def inicio(request):
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_programas = 0
    
    context = {
        'total_aprendices': total_aprendices,
        'total_instructores': total_instructores,
        'total_programas': total_programas,
    }
    
    template = loader.get_template('inicio.html')
    return render(request, 'inicio.html', context)
