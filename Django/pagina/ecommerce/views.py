from django.shortcuts import render
from store.models import Product

def index(request):
    
    productos = Product.objects.all().filter(is_available=True)
    
    context = {'products':productos}
    
    return render(request, 'leonel/index.html', context)