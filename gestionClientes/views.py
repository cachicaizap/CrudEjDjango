from django.shortcuts import render
from django.http import HttpResponse
from gestionClientes.models import Clientes

# Create your views here.

def buscar_cliente(request):
    return render(request,"buscar_cliente.html")

def buscar(request):
    if request.GET["nombre"]:
        #mensaje='Cliente buscado: %r' %request.GET['nombre']
        cliente=request.GET["nombre"]
        clientes= Clientes.objects.filter(nombre__icontains=cliente)

        return render(request,"resultado_busqueda.html",{"clientes":clientes, "query": cliente})
    else:
        mensaje='No envió ningun nombre'

    return HttpResponse(mensaje)