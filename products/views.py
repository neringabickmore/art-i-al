from django.shortcuts import render, get_object_or_404
from .models import Product, Collection, Category

from .forms import ProductForm


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


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)


def add_product(request):
    """ Add a product to the store """
    
    form = ProductForm()
        
    template = 'products/add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)