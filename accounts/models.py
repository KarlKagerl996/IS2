from django.db import models
from django.contrib.auth.models import AbstractUser
from proyectos.models import Proyecto
from Rol.models import Rol
# Create your models here.
class User(AbstractUser):
    cedula = models.CharField(max_length=200)
    id_rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING,  default=1)
    telefono = models.CharField(max_length=200)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

