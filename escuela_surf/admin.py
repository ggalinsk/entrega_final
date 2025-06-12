from django.contrib import admin
from .models import Alumno, Membresia, Clase


admin.site.register(Clase)

@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'tipo_plan', 'fecha_inicio', 'fecha_fin', 'activa')
    list_filter = ('tipo_plan', 'activa')
    search_fields = ('alumno__user__username',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'fecha_alta')
    filter_horizontal = ('clases',)  


