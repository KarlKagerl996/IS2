from django.db import models
from proyectos.models import Proyecto

# Create your models here.
class LineaBase(models.Model):
    "Modelo de una LineaBase"
    estado = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fase = models.CharField(max_length=200)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'LineaBase'
        verbose_name_plural = 'LineasBase'

    def __str__(self):
        return self.nombre
