from django.http import HttpResponse
from django.template import Template,Context,loader


diccionario={ "nombre":"Martin Leandro","apellido":"Martinez","lista_de_notas":[1,9,3,10,5,6,7]}


# sin template loader
# def index(request):
#     archivo=open(r"C:\Users\mlmh3\onedrive\escritorio\programacion\coderhouse\Python\tercera_entrega\plantillas\index.html")
#     contenido=archivo.read()
#     archivo.close
#     template=Template(contenido)
#     contexto=Context(diccionario)
#     documento=template.render(contexto)
#     return HttpResponse(documento)
    



def inicio(request):
    template=loader.get_template("index.html")
    documento=template.render(diccionario)
    return HttpResponse(documento) 

