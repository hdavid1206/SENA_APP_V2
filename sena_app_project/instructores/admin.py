from django.contrib import admin
from .models import Instructor

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = [
        'codigo_instructor',
        'nombre_completo',
        'documento_identidad',
        'especialidad',
        'estado',
        'modalidad_trabajo',
        'fecha_ingreso'
    ]
    
    list_filter = [
        'estado',
        'modalidad_trabajo',
        'especialidad',
        'ciudad',
        'nivel_educativo',
        'fecha_ingreso'
    ]
    
    search_fields = [
        'nombres',
        'apellidos',
        'documento_identidad',
        'correo_electronico',
        'codigo_instructor',
        'especialidad'
    ]
    
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    
    fieldsets = (
        ('Información Personal', {
            'fields': (
                ('tipo_documento', 'documento_identidad'),
                ('nombres', 'apellidos'),
                'fecha_nacimiento',
            )
        }),
        ('Información de Contacto', {
            'fields': (
                'correo_electronico',
                ('telefono_principal', 'telefono_secundario'),
                'ciudad',
                'direccion',
            )
        }),
        ('Información Académica', {
            'fields': (
                'nivel_educativo',
                'titulo_profesional',
                'universidad',
            )
        }),
        ('Información Laboral', {
            'fields': (
                'especialidad',
                'experiencia_anos',
                ('modalidad_trabajo', 'estado'),
            )
        }),
        ('Información Administrativa', {
            'fields': (
                'codigo_instructor',
                'fecha_ingreso',
            )
        }),
        ('Control de Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    list_per_page = 25
    date_hierarchy = 'fecha_ingreso'
    
    def nombre_completo(self, obj):
        return obj.nombre_completo
    nombre_completo.short_description = 'Nombre Completo'
    nombre_completo.admin_order_field = 'apellidos'