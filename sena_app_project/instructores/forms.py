from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__' # Esto incluye automáticamente todos los campos del modelo
        # Alternativamente, puedes listar los campos que quieres:
        # fields = [
        #     'tipo_documento', 'documento_identidad', 'nombres', 'apellidos',
        #     'correo_electronico', 'telefono_principal', 'fecha_nacimiento',
        #     'ciudad', 'direccion', 'nivel_educativo', 'titulo_profesional',
        #     'universidad', 'especialidad', 'experiencia_anos',
        #     'modalidad_trabajo', 'estado', 'fecha_ingreso', 'codigo_instructor',
        # ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})