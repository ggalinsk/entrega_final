from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    fecha_alta = models.DateField(auto_now_add=True)
    notificaciones = models.BooleanField(default=True)
    clases = models.ManyToManyField('Clase', blank=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Membresia(models.Model):
    TIPOS_PLAN = [
        ('mensual', 'Mensual'),
        ('trimestral', 'Trimestral'),
        ('pase_libre', 'Pase libre'),
        ('clases_sueltas', 'Clases sueltas'),
    ]

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tipo_plan = models.CharField(max_length=20, choices=TIPOS_PLAN)
    activa = models.BooleanField(default=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.get_tipo_plan_display()} - {self.alumno}"

class Clase(models.Model):
    DIA_SEMANAL = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    dia = models.CharField(max_length=10, choices=DIA_SEMANAL)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    profe = models.CharField(max_length=100)  # Texto simple

    def __str__(self):
        return f"{self.dia} {self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')} con {self.profe}"