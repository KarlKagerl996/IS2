from django.conf.urls import url, include
from LineaBase.views import LineaBase_view


urlpatterns=[
    url('agregarLineaBase/',LineaBase_view,name='crearlineabase'),
    path('modificarLineabase/<pk>/',LineaBaseUpdate.as_view(), name='modificarlineabase'),


]
