from django.shortcuts import render
from .models import Product, Collection


def gallery(request):
    """ A view to show all products"""

    products = Product.objects.all().order_by('collection_name')

    context = {
        'products': products,
    }
    
    return render(request, 'products/gallery.html', context)


def shop(request):
    """ A view to show all products available to buy"""

    products = Product.objects.all().order_by('tag')

    context = {
        'products': products,
    }
    
    return render(request, 'products/shop.html', context)