from django import forms

class sucursalForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    direccion=forms.CharField( max_length=250)

class clienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    dni=forms.IntegerField()
    direccion=forms.CharField(max_length=250)

class productoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    precio=forms.IntegerField()
    marca=forms.CharField(max_length=50)
    stock=forms.BooleanField()
    imagen=forms.CharField(max_length=250)

class empleadosForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    dni=forms.IntegerField()
    ingreso=forms.DateField()
    