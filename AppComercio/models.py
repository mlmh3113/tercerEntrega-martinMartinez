from django.db import models

class Productos(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    marca=models.CharField(max_length=50)
    stock=models.BooleanField()
    imagen=models.CharField(max_length=250)
    def __str__(self):
        return f"{self.nombre}-{self.marca}"
    

class Empleados(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    ingreso=models.DateField()
    def __str__(self):
        return f"{self.apellido} {self.nombre}"
    

class Sucursales(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=250)
    def __str__(self):
        return self.nombre
    

class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    direccion=models.CharField(max_length=250)
    def __str__(self):
        return f"{self.apellido} {self.nombre} - {self.dni}"
    
    

