from django.db import models
from LineaBase.models import LineaBase

# Create your models here.
class Item(models.Model):
    "Modelo de una Item"
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    version= models.CharField(max_length=200)
    id_lb = models.ForeignKey(LineaBase, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'items'

    def __str__(self):
        return self.nombre
