from django.db import models
from Roles.models import Rol

# Create your models here.
class Permiso(models.Model):
    id_rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING)
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    def __str__ (self):
        return self.tipo
 