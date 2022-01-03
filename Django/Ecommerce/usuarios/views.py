from django.shortcuts import render
from . import models

# Create your views here.

def usuarios(request):
    
    usuarios = models.Usuario.objects.all()
    
    contexto = {'usuarios':usuarios}
    
    return render(request, 'usuarios/usuarios.html', contexto)

def registro(request):
    pass

def login(request):
    pass