from django.db import models

class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('TI', 'Tarjeta de Identidad'),
        ('PP', 'Pasaporte'),
    ]
    
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
        ('VACACIONES', 'En Vacaciones'),
        ('LICENCIA', 'En Licencia'),
    ]
    
    MODALIDAD_CHOICES = [
        ('PRESENCIAL', 'Presencial'),
        ('VIRTUAL', 'Virtual'),
        ('MIXTA', 'Mixta'),
    ]

    # Información Personal
    tipo_documento = models.CharField(
        max_length=2, 
        choices=TIPO_DOCUMENTO_CHOICES, 
        default='CC',
        verbose_name='Tipo de Documento'
    )
    documento_identidad = models.CharField(
        max_length=20, 
        unique=True,
        verbose_name='Número de Documento'
    )
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    
    # Información de Contacto
    correo_electronico = models.EmailField(
        unique=True,
        verbose_name='Correo Electrónico'
    )
    telefono_principal = models.CharField(
        max_length=15,
        verbose_name='Teléfono Principal'
    )
    telefono_secundario = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Teléfono Secundario'
    )
    
    # Información de Ubicación
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    direccion = models.TextField(verbose_name='Dirección')
    
    # Información Académica
    nivel_educativo = models.CharField(
        max_length=100,
        verbose_name='Nivel Educativo',
        help_text='Ej: Licenciado, Ingeniero, Magíster, Doctor'
    )
    titulo_profesional = models.CharField(
        max_length=150,
        verbose_name='Título Profesional'
    )
    universidad = models.CharField(
        max_length=100,
        verbose_name='Universidad/Institución'
    )
    
    # Información Laboral
    especialidad = models.CharField(
        max_length=100,
        verbose_name='Área de Especialidad'
    )
    experiencia_anos = models.PositiveIntegerField(
        verbose_name='Años de Experiencia'
    )
    modalidad_trabajo = models.CharField(
        max_length=10,
        choices=MODALIDAD_CHOICES,
        default='PRESENCIAL',
        verbose_name='Modalidad de Trabajo'
    )
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='ACTIVO',
        verbose_name='Estado'
    )
    
    # Información Administrativa
    fecha_ingreso = models.DateField(verbose_name='Fecha de Ingreso')
    codigo_instructor = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Código de Instructor'
    )
    
    # Campos de Control
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.especialidad}"
    
    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"
    
    @property
    def edad(self):
        from datetime import date
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
    
    def get_estado_display_color(self):
        colors = {
            'ACTIVO': 'success',
            'INACTIVO': 'danger', 
            'VACACIONES': 'warning',
            'LICENCIA': 'info'
        }
        return colors.get(self.estado, 'secondary')