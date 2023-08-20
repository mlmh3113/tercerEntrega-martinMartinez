from django.contrib import admin
from .models import Clientes,Empleados,Productos,Sucursales

admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Empleados)
admin.site.register(Sucursales)
