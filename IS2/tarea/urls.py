from django.urls import path
import views

urlpatterns = [
    path('registrar_tarea',views.registrar_tarea,name='registrar_tarea'),
    path('listar_tarea',views.listar_tarea,name='listar_tarea')
]
