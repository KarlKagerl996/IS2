from django.db import models

# Create your models here.
class Tarea(models.Model):
    version = models.CharField(max_length=10)

    PRIORIDAD_TAREA = (
        ('Alta','Alta'),
        ('Baja','Baja'),
        ('Normal','Normal')
    )

    ESTADOS_TAREA = (
        ('Iniciado','Iniciado'),
        ('Pendiente','Pendiente'),
        ('Finalizado','Finalizado'),
    )

    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_TAREA)
    estado = models.CharField(max_length=50, choices=ESTADOS_TAREA)
    descripcion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100)
    id_tarea_padre = models.IntegerField(null=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
