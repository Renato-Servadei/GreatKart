from django.shortcuts import render
from store.models import Product

def store(request):
    products = Product.objects.all().filter(is_available = True)
    
    return render(request, 'store/store.html', context = {
        'products' : products
    })
