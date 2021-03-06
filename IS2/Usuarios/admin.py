from django.contrib import admin
from .models import Usuario

# Register your models here.

#from django.contrib.auth.models import User, Group
#
#
#admin.site.unregister(User)
#admin.site.unregister(Group)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido')
    list_display_links = ('cedula',)
    list_filter = ('cedula',)
    search_fields = ('cedula',)



admin.site.register(Usuario, UsuarioAdmin)

