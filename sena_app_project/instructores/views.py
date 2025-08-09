from django.shortcuts import render, get_object_or_404
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
    # Usamos el atajo render directamente
    return render(request, 'lista_instructores.html', context)

def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)

    cursos_coordinados = instructor.cursos_coordinados.all()
    cursos_impartidos = instructor.cursos_impartidos.all()
    
    context = {
        'instructor': instructor,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos,
    }
    
    return render(request, 'detalle_instructor.html', context)
    
    

