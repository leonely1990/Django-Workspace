from django.shortcuts import render, get_object_or_404
from .models import Product
from categoria.models import Categoria

# Create your views here.

def store(request, category_slug=None):
    
    categories = None
    productos = None
    
    if category_slug != None:
        categories = get_object_or_404(Categoria, slug=category_slug)
        productos = Product.objects.filter(category=categories, is_available=True)
        productos_cant = productos.count()  
    else:       
        productos = Product.objects.all().filter(is_available=True)
        productos_cant = productos.count()
    
    context = {
        'products': productos,
        'cant': productos_cant
    }
    
    return render(request, 'store/index.html', context)