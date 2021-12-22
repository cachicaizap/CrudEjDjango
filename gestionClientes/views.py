from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from gestionClientes.models import Clientes
from gestionClientes.forms import FormularioCliente

# Create your views here.

def listarClientes(request):
    clientes=Clientes.objects.all()
    return render(request,"gestionClientes/verCliente.html",{"clientes":clientes})

def crearCliente(request):
    if request.method=="POST":
        miFormulario=FormularioCliente(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            newCliente=Clientes.objects.create(nombre=infForm['nombre'], direccion=infForm['direccion'], email=infForm['email'], tfno=infForm['tfno'])
        request.method=""
        clientes=Clientes.objects.all()
        return redirect("/")
    else:
        miFormulario=FormularioCliente()
        return render(request,"gestionClientes/crearCliente.html",{"formulario":miFormulario })

def editarCliente(request):
    if request.method=="POST":
        miFormulario=FormularioCliente(request.POST)
        cod=request.GET.get('id')
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            cliente=Clientes.objects.get(id=cod)

            cliente.nombre=infForm['nombre']
            cliente.direccion=infForm['direccion']
            cliente.email=infForm['email']
            cliente.tfno=infForm['tfno']
            cliente.save()
        return redirect("/")
    if request.method=="GET":
        cod=request.GET.get('id')
        cliente=Clientes.objects.get(id=cod)
        miFormulario=FormularioCliente({'nombre':cliente.nombre, 'direccion':cliente.direccion, 'email': cliente.email, 'tfno':cliente.tfno})
        request.method=""
        return render(request,"gestionClientes/editarCliente.html",{"formulario":miFormulario,"id":cod})

def eliminarCliente(request,codigo):
    cliente=Clientes.objects.get(id=codigo)
    cliente.delete()
    return redirect('/')
            