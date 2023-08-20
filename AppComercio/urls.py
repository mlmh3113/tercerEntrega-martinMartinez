from django.urls import path
from .views import *


urlpatterns = [
    path("productos/",productos,name="productos"),
    path("empleados/",empleados,name="empleados"),
    path("sucursales/",sucursales,name="sucursales"),
    path("clientes/",cliente,name="cliente"),
    path("busquedaSuc/",busquedaSuc,name="busquedaSuc"),
]
