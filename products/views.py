import sweetify

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Collection, Category, Image, ImagesFolder

from .forms import ProductForm, CollectionForm, ImagesFolderForm, ImageForm

from bag.contexts import bag_contents

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
    # do not remove this else view bag button won't show
    bag = request.session.get('bag', {})

    context = {
        'product': product,
        'bag': bag,
    }

    return render(request, 'products/product-detail.html', context)


@login_required
def product_management(request):
    """ Manage products """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    return render(request, 'products/prod-mngmnt/product-management.html')


@login_required
def view_all_collections(request):
    """ View all collections """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('product_management'))
    
    collections = Collection.objects.all()
    template = 'products/prod-mngmnt/view-all-collections.html'
    context = {
        'collections': collections,
    }
    return render(request, template, context)


@login_required
def add_collection(request):
    """ Add new collection name """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))
    
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
       
    template = 'products/prod-mngmnt/add-collection.html'
    context = {
        'collection_form': collection_form,
    }

    return render(request, template, context)


@login_required
def edit_collection(request, name):
    """ Edit collection name """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    collection = get_object_or_404(Collection, name=name)
    if request.method == 'POST':
        collection_form = CollectionForm(request.POST, instance=collection)
        if collection_form.is_valid():
            collection_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
                text= "Successfully updated collection name!")
            return redirect(reverse('view_all_collections'))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
                text= "Failed to update collection name. Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        collection_form = CollectionForm(instance=collection)
        sweetify.sweetalert(request, title=f"You are editing collection: {collection.friendly_name}", icon='info')
    
    template = 'products/prod-mngmnt/edit-collection.html'
    context = {
        'collection_form': collection_form,
        'collection': collection,
    }

    return render(request, template, context)


@login_required
def view_all_images(request):
    """ View all images """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))
    
    images = Image.objects.all()
    template = 'products/prod-mngmnt/view-all-images.html'
    context = {
        'images': images,
    }
    return render(request, template, context)


@login_required
def add_img(request):
    """ Add new image """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        img_form = ImageForm(request.POST, request.FILES)
        if img_form.is_valid():
            img = img_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
            text= "Successfully added new image!",
            timer=2000, timerProgressBar='true', persistent="Close")
            return redirect(reverse('add_img'))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
            text= "Failed to add new image. Please ensure the form is valid.",
            timer=2000, timerProgressBar='true', persistent="Close")

    else:
        img_form = ImageForm()
       
    template = 'products/prod-mngmnt/add-image.html'
    context = {
        'img_form': img_form,
    }

    return render(request, template, context)


@login_required
def edit_img(request, name):
    """ Edit image name """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))
    
    img = get_object_or_404(Image, name=name)
    if request.method == 'POST':
        img_form = ImageForm(request.POST, request.FILES, instance=img)
        if img_form.is_valid():
            img_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
                text= "Successfully updated the image details!")
            return redirect(reverse('view_all_images'))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
                text= "Failed to update image details. Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        img_form = ImageForm(instance=img)
        sweetify.sweetalert(request, title='info', icon='info',
                text= f"You are editing image: {img.name}")
    
    template = 'products/prod-mngmnt/edit-image.html'
    context = {
        'img_form': img_form,
        'img': img,
    }

    return render(request, template, context)


@login_required
def add_img_folder(request):
    """ Add new images folder and select images """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))
    
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
       
    template = 'products/prod-mngmnt/add-img-folder.html'
    context = {
        'img_folder_form': img_folder_form,
    }

    return render(request, template, context)


@login_required
def view_all_folders(request):
    """ View all images folders """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))
    
    folders = ImagesFolder.objects.all()
    template = 'products/prod-mngmnt/view-all-folders.html'
    context = {
        'folders': folders,
    }
    return render(request, template, context)


@login_required
def edit_img_folder(request, name):
    """ Edit images folder """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    img_folder = get_object_or_404(ImagesFolder, name=name)
    if request.method == 'POST':
        img_folder_form = ImagesFolderForm(request.POST, instance=img_folder)
        if img_folder_form.is_valid():
            img_folder_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
                text= "Successfully updated images folder content!")
            return redirect(reverse('view_all_folders'))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
                text= "Failed to update images folder content. Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        img_folder_form = ImagesFolderForm(instance=img_folder)
        sweetify.sweetalert(request, title='info', icon='info',
                text= f"You are editing images folder: {img_folder.name}")
    
    template = 'products/prod-mngmnt/edit-img-folder.html'
    context = {
        'img_folder_form': img_folder_form,
        'img_folder': img_folder,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Add a new product to the gallery """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        prod_form = ProductForm(request.POST, request.FILES)
        if prod_form.is_valid():
            product = prod_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
            text= "Successfully added product!",
            timer=2000, timerProgressBar='true', persistent="Close")
            return redirect(reverse('product_detail', args=[product.name]))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
            text= "Failed to add product. Please ensure the form is valid.",
            timer=2000, timerProgressBar='true', persistent="Close")

    else:
        prod_form = ProductForm()
       
    template = 'products/prod-mngmnt/add-product.html'
    context = {
        'prod_form': prod_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, name):
    """ Edit product details """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    product = get_object_or_404(Product, name=name)
    if request.method == 'POST':
        prod_form = ProductForm(request.POST, instance=product)
        if prod_form.is_valid():
            prod_form.save()
            sweetify.sweetalert(request, title='success', icon='success',
                text= "Successfully updated product details!",
                timer=2000)
            return redirect(reverse('product_detail', args=[product.name]))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
                text= "Failed to update product details. Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        prod_form = ProductForm(instance=product)
        sweetify.sweetalert(request, title='info', icon='info',
                text= f"You are editing product: {product.name}",
                timer=2000)
    
    template = 'products/prod-mngmnt/edit-product.html'
    context = {
        'prod_form': prod_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, name):
    """ Delete product """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    product = get_object_or_404(Product, name=name)
    product.delete()
    sweetify.sweetalert(request, title='success', icon='success',
                text= "Successfully deleted the product!",
                timer=2000)
    return redirect(reverse('gallery'))
