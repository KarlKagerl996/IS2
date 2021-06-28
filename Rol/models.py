from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol= models.CharField(max_length=50) 
    estado= models.CharField(max_length=50) 
    def __str__ (self):
        return self.nombre_rol
