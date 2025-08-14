from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Instructor
from .forms import InstructorForm

def lista_instructores(request):
    instructores = Instructor.objects.all()
    context = {'instructores': instructores}
    return render(request, 'lista_instructores.html', context)

def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    context = {'instructor': instructor}
    return render(request, 'detalle_instructor.html', context)

def crear_instructor(request):
    """
    Vista para crear un nuevo instructor.
    Maneja el envío del formulario GET y POST.
    """
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save() # <-- Se guarda el objeto de forma automática
            messages.success(request, 'Instructor agregado exitosamente.')
            return redirect('instructores:lista_instructores')
        else:
            messages.error(request, 'Hubo un error al crear el instructor. Por favor, revise los campos.')
    else:
        form = InstructorForm()
    
    context = {'form': form}
    return render(request, 'crear_instructor.html', context)