from django.shortcuts import render
from .models import Product, Collection


def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all().order_by('collection_name')

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)
