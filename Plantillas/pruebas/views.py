from django.shortcuts import render

def index(request):
    return render(request, 'Mockup01/template.html')