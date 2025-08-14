from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import ProgramaForm
from .models import Programa

# Vista para la lista de programas
def programas(request):
    programas_list = Programa.objects.all()
    return render(request, 'programas/lista_programas.html', {'programas_list': programas_list})

# Vista para crear un programa
class ProgramaCreateView(CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'programas/crear_programa.html'
    success_url = reverse_lazy('programas:lista_programas')

# Vista para la lista de programas usando la vista genérica
class ProgramaListView(ListView):
    model = Programa
    template_name = 'programas/lista_programas.html'
    context_object_name = 'programas_list'