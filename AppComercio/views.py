from django.shortcuts import render
from .models import *
from .forms import *


def productos(request):
    data=Productos.objects.all()
    if request.method=="POST":
        form=productoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            precio=info["precio"]
            marca=info["marca"]
            stock=info["stock"]
            imagen=info["imagen"]
            producto=Productos(nombre=nombre,precio=precio,marca=marca,stock=stock,imagen=imagen)
            producto.save()
            form_producto=productoForm()
            return render(request,"AppComercio/productos.html",{"productos":data,"mensaje":"Producto Cargado","formulario":form_producto})
        return render(request,"AppComercio/productos.html",{"mensaje":"producto invalido",})
    else:
        form_producto=productoForm()
        return render(request,"AppComercio/productos.html",{"productos":data,"productos":data,"formulario":form_producto})


def empleados(request):
    data=Empleados.objects.all()
    if request.method=="POST":
        form=empleadosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            dni=info["dni"]
            ingreso=info["ingreso"]
            empleado=Empleados(nombre=nombre,apellido=apellido,dni=dni,ingreso=ingreso)
            empleado.save()
            form_empleado=empleadosForm()
            return render(request,"AppComercio/empleados.html",{"mensaje":"Empleado Creado","formulario":form_empleado,"empleados":data})
        return render(request,"AppComercio/empleados.html",{"mensaje":"usuario invalido","empleados":data})
    else:
        form_empleado=empleadosForm()
        return render(request,"AppComercio/empleados.html",{"empleados":data,"formulario":form_empleado})


def sucursales(request):
    data=Sucursales.objects.all()
    if request.method=="POST":
        form=sucursalForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            direccion=info["direccion"]
            sucursal=Sucursales(nombre=nombre,direccion=direccion)
            sucursal.save()
            form_sucursal=sucursalForm()
            return render(request,"AppComercio/sucursales.html",{"mensaje":"Sucursal Cargada","sucursales":data,"formulario":form_sucursal})
        return render(request,"AppComercio/sucursales.html",{"mensaje":"sucursasle invalida","formulario":form_sucursal})
    else:
        form_sucursal=sucursalForm()
        return render(request,"AppComercio/sucursales.html",{"sucursales":data,"formulario":form_sucursal})


def cliente(request):
    data=Clientes.objects.all()
    if request.method=="POST":
        form=clienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            dni=info["dni"]
            direccion=info["direccion"]
            cliente=Clientes(nombre=nombre,apellido=apellido,dni=dni,direccion=direccion)
            cliente.save()
            form_cliente=clienteForm()   
            return render(request,"AppComercio/cliente.html",{"mensaje":"Cliente Agregado","formulario":form_cliente,"clientes":data}) 
        return render(request,"AppComercio/cliente.html",{"mensaje":"cliente invalido","clientes":data}) 
    else:
        form_cliente=clienteForm()   
        return render(request,"AppComercio/cliente.html",{"formulario":form_cliente,"clientes":data})  


def busquedaSuc(request):
    if request.method=="POST":
        sucursal=request.POST["sucursal"]
        if sucursal != "":
         data=Sucursales.objects.filter(nombre__icontains=sucursal)
         print(data)
         if data:
            return render(request,"AppComercio/busquedaSuc.html",{"data":data})
         else:
             return render(request,"AppComercio/busquedaSuc.html",{"mensaje":"No se encuentran datos"})
        
    return render(request,"AppComercio/busquedaSuc.html")  
