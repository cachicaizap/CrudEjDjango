from django import forms

class FormularioCliente(forms.Form):
    nombre=forms.CharField()
    direccion=forms.CharField()
    email=forms.EmailField()
    tfno=forms.CharField()