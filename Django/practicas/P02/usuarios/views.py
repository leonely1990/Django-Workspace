from django.shortcuts import render
from . import models

# Create your views here.

def usuariolist(request):
    
    usuarios = models.Usuario.objects.all()
    
    lista = {"usuarios":usuarios}
    
    return render(request, 'usuarios/listausuarios.html', lista)