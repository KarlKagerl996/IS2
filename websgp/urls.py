"""websgp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (home, logoutUser, crear_usuario, ListarUsuariosView, 
                            UserUpdate, eliminar_usuario, listar_asignar, UpdateProyecto)
from django.urls import include, path
from proyectos.views import proyecto_view, ProyectoListView, ProyectoUpdate, eliminar_proyecto
from LineaBase.views import LineaBase_view, LineaBaseListView, LineaBaseUpdate, eliminar_lineabase
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from items.views import item_add, ItemListView, ItemUpdate, eliminar_item

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', home, name='index'),
    path('logout/', logoutUser, name='logout'),
    path('agregar_proyectos/', login_required(proyecto_view), name='crearproyecto'),
    path('listar_proyectos/', login_required(ProyectoListView.as_view()), name='listaproyectos'),
    path('editar_proyectos/<pk>/',login_required(ProyectoUpdate.as_view()), name='editarproyecto'),
    path('eliminar_proyecto/<int:id>/', login_required(eliminar_proyecto), name='eliminarproyecto'),
    url('agregar_lineabase/',LineaBase_view,name='crearlineabase'),
    path('listar_lineabase/', login_required(LineaBaseListView.as_view()), name='listalineabase'),
    path('editar_lineabase/<pk>/',login_required(LineaBaseUpdate.as_view()), name='modificarlineabase'),
    path('eliminar_lineabase/<int:id>/', login_required(eliminar_lineabase), name='eliminarlineabase'),
    path('listar_items/<id_lbase>/', ItemListView.as_view(),name="listaritems"),
    path('agregar_item/<int:id>/', item_add, name='crearitem'),
    path('editar_items/<pk>/', login_required(ItemUpdate.as_view()), name='modificaritem'),
    path('eliminar_item/<int:id>/', login_required(eliminar_item), name='eliminaritem'),
    path('crear_usuario/', crear_usuario, name='crearusuario'),
    path('listar_usuarios/', login_required(ListarUsuariosView.as_view()), name='listausuarios'),
    path('editar_usuarios/<pk>/', UserUpdate.as_view(), name='editarusuario'),
    path('eliminar_usuario/<int:id>/', eliminar_usuario, name='eliminarusuario'),
    path('lista_asignar', listar_asignar, name='listarasignar'),
    path('asginar_proyecto/<pk>/', UpdateProyecto.as_view(), name='asignarproyecto'),
]
