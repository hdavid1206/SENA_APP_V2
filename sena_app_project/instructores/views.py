from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Instructor
from .forms import InstructorForm

def lista_instructores(request):
    """
    Vista para listar todos los instructores.
    """
    instructores = Instructor.objects.all()
    context = {'instructores': instructores}
    return render(request, 'lista_instructores.html', context)

def detalle_instructor(request, instructor_id):
    """
    Vista para mostrar los detalles de un instructor específico.
    """
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
            Instructor.objects.create(
                tipo_documento=form.cleaned_data['tipo_documento'],
                documento_identidad=form.cleaned_data['documento_identidad'],
                nombres=form.cleaned_data['nombre'],
                apellidos=form.cleaned_data['apellido'],
                telefono_principal=form.cleaned_data['telefono'],
                correo_electronico=form.cleaned_data['correo'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                ciudad=form.cleaned_data['ciudad'],
                direccion=form.cleaned_data['direccion'],
                nivel_educativo=form.cleaned_data['nivel_educativo'],
                titulo_profesional=form.cleaned_data['titulo_profesional'],
                universidad=form.cleaned_data['universidad'],
                especialidad=form.cleaned_data['especialidad'],
                experiencia_anos=form.cleaned_data['anos_experiencia'],
                modalidad_trabajo=form.cleaned_data['modalidad_trabajo'],
                fecha_ingreso=form.cleaned_data['fecha_ingreso'],
                codigo_instructor=form.cleaned_data['codigo_instructor']
            )
            messages.success(request, 'Instructor creado exitosamente.')
            return redirect('instructores:lista_instructores')
        else:
            messages.error(request, 'Hubo un error al crear el instructor. Por favor, revise los campos.')
    else:
        form = InstructorForm()
    
    context = {'form': form}
    return render(request, 'crear_instructor.html', context)