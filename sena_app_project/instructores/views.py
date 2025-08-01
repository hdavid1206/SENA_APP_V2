from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Instructor

def lista_instructores(request):

    lista_instructores = Instructor.objects.all().order_by('apellidos', 'nombres')
    total_instructores = lista_instructores.count()
    
    instructores_activos = lista_instructores.filter(estado='ACTIVO').count()
    instructores_presenciales = lista_instructores.filter(modalidad_trabajo='PRESENCIAL').count()
    instructores_virtuales = lista_instructores.filter(modalidad_trabajo='VIRTUAL').count()
    
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': total_instructores,
        'instructores_activos': instructores_activos,
        'instructores_presenciales': instructores_presenciales,
        'instructores_virtuales': instructores_virtuales,
    }
    
    return render(request, 'lista_instructores.html', context)

def detalle_instructor(request, instructor_id):

    try:
        instructor = Instructor.objects.get(pk=instructor_id)
    except Instructor.DoesNotExist:
        return render(request, '404.html', {'mensaje': 'Instructor no encontrado'})
    
    context = {
        'instructor': instructor,
    }
    
    return render(request, 'detalle_instructor.html', context)