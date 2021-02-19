from django.db import models
from Roles.models import Rol
# Create your models here.

#cedula: VARCHAR NOT NULL [ PK ]
#id_rol: NUMERIC NOT NULL [ FK ]
#nombre: VARCHAR NOT NULL
#apellido: VARCHAR NOT NULL
#email: VARCHAR NOT NULL
#username: VARCHAR NOT NULL
#password: VARCHAR NOT NULL
#telefono: VARCHAR NOT NULL
class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True)
    id_rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING)
    nombre = models.CharField(max_length=50,null=False)
    apellido = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False)
    telefono = models.CharField(max_length=50 )
    def __str__ (self):
        return self.nombre

    

