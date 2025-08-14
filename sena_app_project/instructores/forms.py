from django import forms
from .models import Instructor

class InstructorForm(forms.Form):
    tipo_documento = forms.CharField(max_length=50)
    documento_identidad = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=100, label="Nombres")
    apellido = forms.CharField(max_length=100, label="Apellidos")
    telefono = forms.CharField(max_length=15, label="Teléfono Principal")
    correo = forms.EmailField(label="Correo Electrónico")
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")
    ciudad = forms.CharField(max_length=100)
    direccion = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label="Dirección")
    nivel_educativo = forms.CharField(max_length=100)
    titulo_profesional = forms.CharField(max_length=255)
    universidad = forms.CharField(max_length=255)
    especialidad = forms.CharField(max_length=255)
    anos_experiencia = forms.IntegerField(label="Años de Experiencia")
    modalidad_trabajo = forms.CharField(max_length=50)
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Ingreso")
    codigo_instructor = forms.CharField(max_length=50)
    
    def clean(self):
        cleaned_data = super().clean()
        documento = cleaned_data.get('documento_identidad')
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')

        if not documento or not nombre or not apellido:
            raise forms.ValidationError("Todos los campos son obligatorios.")

        return cleaned_data

    def clean_documento_identidad(self):
        documento = self.cleaned_data['documento_identidad']
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento
        
        
    def save(self):
        try:
            instructor = Instructor.objects.create(
                documento_identidad=self.cleaned_data['documento_identidad'],
                tipo_documento=self.cleaned_data['tipo_documento'],
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                telefono=self.cleaned_data.get('telefono', ''),
                correo=self.cleaned_data.get('correo', ''),
                fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
                ciudad=self.cleaned_data.get('ciudad', ''),
                direccion=self.cleaned_data.get('direccion', ''),
                nivel_educativo=self.cleaned_data['nivel_educativo'],
                especialidad=self.cleaned_data['especialidad'],
                anos_experiencia=self.cleaned_data['anos_experiencia'],
                activo=self.cleaned_data.get('activo', True),
                fecha_vinculacion=self.cleaned_data['fecha_vinculacion'],
                fecha_registro=self.cleaned_data['fecha_registro']
            )
            return instructor
        except Exception as e:
            raise forms.ValidationError(f"Error al crear el instructor: {str(e)}")