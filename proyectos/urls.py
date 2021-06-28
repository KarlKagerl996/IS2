from django.conf.urls import url, include
from proyectos.views import proyecto_view


urlpatterns=[
    url('agregarProyecto/',proyecto_view,name='crearproyecto'),
    path('editarProyecto/<pk>/',ProyectoUpdate.as_view(), name='editarproyecto'),


]