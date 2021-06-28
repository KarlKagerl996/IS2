from django.db import models


# Create your models here.
class Proyecto(models.Model):
    "Modelo de un proyecto"
    nombre = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    fecha=models.DateField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre   