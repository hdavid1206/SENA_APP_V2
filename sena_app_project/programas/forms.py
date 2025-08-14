from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            'codigo', 'nombre', 'nivel_formacion', 'modalidad',
            'duracion_meses', 'duracion_horas', 'descripcion',
            'competencias', 'perfil_egreso', 'requisitos_ingreso',
            'centro_formacion', 'regional', 'estado', 'fecha_creacion'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'competencias': forms.Textarea(attrs={'rows': 3}),
            'perfil_egreso': forms.Textarea(attrs={'rows': 3}),
            'requisitos_ingreso': forms.Textarea(attrs={'rows': 3}),
            'fecha_creacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})