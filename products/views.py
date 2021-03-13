import sweetify

from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Collection, Category

from .forms import ProductForm, CollectionForm, ImagesFolderForm


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


def product_detail(request, name):
    """ A view to show individual product details """

    product = get_object_or_404(Product, name=name)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)


def add_collection(request):
    """ Add new collection name """
    
    if request.method == 'POST':
        collection_form = CollectionForm(request.POST)
        if collection_form.is_valid():
            collection = collection_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
            text= "Successfully added collection name!",
            timer=2000, timerProgressBar='true', persistent="Close")
            return redirect(reverse('add_collection'))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
            text= "Failed to add new collection name. Please ensure the form is valid.",
            timer=2000, timerProgressBar='true', persistent="Close")

    else:
        collection_form = CollectionForm()
       
    template = 'products/add-collection.html'
    context = {
        'collection_form': collection_form,
    }

    return render(request, template, context)


def add_img_folder(request):
    """ Add new collection name """
    
    if request.method == 'POST':
        img_folder_form = ImagesFolderForm(request.POST)
        if img_folder_form.is_valid():
            img_folder = img_folder_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
            text= "Successfully added new folder with selected images!",
            timer=2000, timerProgressBar='true', persistent="Close")
            return redirect(reverse('add_img_folder'))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
            text= "Failed to add new folder. Please ensure the form is valid.",
            timer=2000, timerProgressBar='true', persistent="Close")

    else:
        img_folder_form = ImagesFolderForm()
       
    template = 'products/add-img-folder.html'
    context = {
        'img_folder_form': img_folder_form,
    }

    return render(request, template, context)


def add_product(request):
    """ Add a product to the store """
    
    if request.method == 'POST':
        prod_form = ProductForm(request.POST, request.FILES)
        if prod_form.is_valid():
            product = prod_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
            text= "Successfully added product!",
            timer=2000, timerProgressBar='true', persistent="Close")
            return redirect(reverse('add_product'))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
            text= "Failed to add product. Please ensure the form is valid.",
            timer=2000, timerProgressBar='true', persistent="Close")

    else:
        prod_form = ProductForm()
       
    template = 'products/add-product.html'
    context = {
        'prod_form': prod_form,
    }

    return render(request, template, context)


