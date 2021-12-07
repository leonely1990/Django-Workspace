from django.shortcuts import render

def index(request):
    return render(request, 'leonel/index.html')

def registro(request):
    return render(request, 'register.html')

def iniciar(request):
    return render(request, 'signin.html')