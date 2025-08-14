from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render # Lo dejamos por si lo usas en otro lado
from .models import Programa
from .forms import ProgramaForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

# TU VISTA ORIGINAL - SIN CAMBIOS
def programas(request):
    lista_programas = Programa.objects.all().order_by('nombre')
    template = loader.get_template('lista_programas.html')
    contexto = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    
    return HttpResponse(template.render(contexto, request))

# NUEVA VISTA PARA CREAR PROGRAMAS
class ProgramaCreateView(CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'crear_programa.html'
    template_name = 'programas/crear_programa.html' 
    success_url = reverse_lazy('programas:lista_programas') # Redirige a la lista después de crear

    def form_valid(self, form):
        # Añade un mensaje de éxito
        messages.success(self.request, "El programa se ha registrado exitosamente.")
        return super().form_valid(form)