import sweetify

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Collection, Category, Image, ImagesFolder

from .forms import ProductForm, CollectionForm, ImagesFolderForm, ImageForm

from home.models import SocialMedia
from bag.contexts import bag_contents


def gallery(request):
    """ A view to show all products"""

    products = Product.objects.all().order_by('collection_name')
    social_media = SocialMedia.objects.all()
    template = 'products/gallery.html'
    context = {
        'products': products,
        'all_social_media': social_media,
    }

    return render(request, template, context)


def shop(request):
    """ A view to show all products available to buy"""

    products = Product.objects.all().order_by('tag')
    social_media = SocialMedia.objects.all()
    template = 'products/shop.html'
    context = {
        'products': products,
        'all_social_media': social_media,
    }

    return render(request, template, context)


def product_detail(request, name):
    """ A view to show individual product details """

    product = get_object_or_404(Product, name=name)
    social_media = SocialMedia.objects.all()
    # do not remove this else view bag button won't show
    bag = request.session.get('bag', {})

    show_add_btn = True

    if str(product.id) in bag:
        show_add_btn = False

    template = 'products/product-detail.html'
    context = {
        'show_add_btn': show_add_btn,
        'product': product,
        'bag': bag,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def product_management(request):
    """ Manage products """
    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()
    template = 'products/prod-mngmnt/product-management.html'
    context = {
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Add a new product to the gallery """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    if request.method == 'POST':
        prod_form = ProductForm(request.POST, request.FILES)
        if prod_form.is_valid():
            product = prod_form.save()
            sweetify.sweetalert(
                request, icon='success',
                title="Successfully added product!")
            return redirect(reverse('product_detail', args=[product.name]))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Failed to add product. Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")

    else:
        prod_form = ProductForm()

    template = 'products/prod-mngmnt/add-product.html'
    context = {
        'prod_form': prod_form,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit product details """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        prod_form = ProductForm(request.POST, instance=product)
        if prod_form.is_valid():
            prod_form.save()
            sweetify.sweetalert(
                request, icon='success',
                title="Successfully updated product details!")
            return redirect(reverse('product_detail', args=[product.name]))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Failed to update product details. \
                Please ensure the form is valid.")
    else:
        prod_form = ProductForm(instance=product)
        sweetify.sweetalert(
            request, icon='info',
            title=f"You are editing product: {product.name}")

    template = 'products/prod-mngmnt/edit-product.html'
    context = {
        'prod_form': prod_form,
        'product': product,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def delete_product(request, name):
    """ Delete product """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    product = get_object_or_404(Product, name=name)
    product.delete()
    sweetify.sweetalert(
        request, icon='success',
        title="Successfully deleted the product!")
    return redirect(reverse('gallery'))


@login_required
def view_all_collections(request):
    """ View all collections """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('product_management'))

    collections = Collection.objects.all()
    social_media = SocialMedia.objects.all()

    template = 'products/prod-mngmnt/view-all-collections.html'
    context = {
        'collections': collections,
        'all_social_media': social_media,
    }
    return render(request, template, context)


@login_required
def add_collection(request):
    """ Add new collection name """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    if request.method == 'POST':
        collection_form = CollectionForm(request.POST)
        if collection_form.is_valid():
            collection = collection_form.save()
            sweetify.sweetalert(
                request, icon='success',
                title="Successfully added collection name!")
            return redirect(reverse('view_all_collections'))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Failed to add new collection name. \
                Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")

    else:
        collection_form = CollectionForm()

    template = 'products/prod-mngmnt/add-collection.html'
    context = {
        'collection_form': collection_form,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def edit_collection(request, collection_id):
    """ Edit collection name """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    collection = get_object_or_404(Collection, pk=collection_id)
    if request.method == 'POST':
        collection_form = CollectionForm(
            request.POST, instance=collection)
        if collection_form.is_valid():
            collection_form.save()
            sweetify.sweetalert(
                request, icon='success',
                title="Successfully updated collection name!")
            return redirect(reverse('view_all_collections'))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Failed to update collection name. \
                Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        collection_form = CollectionForm(instance=collection)
        sweetify.sweetalert(
            request, title=f"You are editing \
            collection: {collection.friendly_name}", icon='info')

    template = 'products/prod-mngmnt/edit-collection.html'
    context = {
        'collection_form': collection_form,
        'collection': collection,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def delete_collection(request, name):
    """ Delete collections  """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    collection = get_object_or_404(Collection, name=name)
    collection.delete()
    sweetify.sweetalert(
        request, icon='success',
        title=f"Successfully deleted {collection.name} collection!")
    return redirect(reverse('view_all_collections'))


@login_required
def view_all_images(request):
    """ View all images """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()
    images = Image.objects.all().order_by('name')

    template = 'products/prod-mngmnt/view-all-images.html'
    context = {
        'images': images,
        'all_social_media': social_media,
    }
    return render(request, template, context)


@login_required
def add_img(request):
    """ Add new image """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    if request.method == 'POST':
        img_form = ImageForm(request.POST, request.FILES)
        if img_form.is_valid():
            img = img_form.save()
            sweetify.sweetalert(
                request, icon='success',
                title="Successfully added new image!")
            return redirect(reverse('view_all_images'))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Failed to add new image. \
                Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="close")

    else:
        img_form = ImageForm()

    template = 'products/prod-mngmnt/add-image.html'
    context = {
        'img_form': img_form,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def edit_img(request, image_id):
    """ Edit image name """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    img = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        img_form = ImageForm(
            request.POST, request.FILES,
            instance=img)
        if img_form.is_valid():
            img_form.save()
            sweetify.sweetalert(
                request, icon='success',
                title="Successfully updated the image details!")
            return redirect(reverse('view_all_images'))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Failed to update image details. \
                Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        img_form = ImageForm(instance=img)
        sweetify.sweetalert(
            request, icon='info',
            title=f"You are editing image: {img.name}")

    template = 'products/prod-mngmnt/edit-image.html'
    context = {
        'img_form': img_form,
        'img': img,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def delete_image(request, name):
    """ Delete images  """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    images = get_object_or_404(Image, name=name)
    images.delete()
    sweetify.sweetalert(
        request, icon='success',
        title=f"Successfully deleted {images.name} image!")
    return redirect(reverse('view_all_images'))


@login_required
def add_img_folder(request):
    """ Add new images folder and select images """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    if request.method == 'POST':
        img_folder_form = ImagesFolderForm(request.POST)
        if img_folder_form.is_valid():
            img_folder = img_folder_form.save()
            sweetify.sweetalert(
                request, icon='success',
                title="Successfully added new folder with selected images!")
            return redirect(reverse('view_all_folders'))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Failed to add new folder. \
                Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")

    else:
        img_folder_form = ImagesFolderForm()

    template = 'products/prod-mngmnt/add-img-folder.html'
    context = {
        'img_folder_form': img_folder_form,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def view_all_folders(request):
    """ View all images folders """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    folders = ImagesFolder.objects.all()
    template = 'products/prod-mngmnt/view-all-folders.html'
    context = {
        'folders': folders,
        'all_social_media': social_media,
    }
    return render(request, template, context)


@login_required
def edit_img_folder(request, folder_id):
    """ Edit images folder """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    social_media = SocialMedia.objects.all()

    img_folder = get_object_or_404(ImagesFolder, pk=folder_id)
    if request.method == 'POST':
        img_folder_form = ImagesFolderForm(
            request.POST, instance=img_folder)
        if img_folder_form.is_valid():
            img_folder_form.save()
            sweetify.sweetalert(
                request, icon='success',
                title="Successfully updated images folder content!")
            return redirect(reverse('view_all_folders'))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Failed to update images folder \
                content. Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        img_folder_form = ImagesFolderForm(instance=img_folder)
        sweetify.sweetalert(
            request, icon='info',
            title=f"You are editing images folder: {img_folder.name}")

    template = 'products/prod-mngmnt/edit-img-folder.html'
    context = {
        'img_folder_form': img_folder_form,
        'img_folder': img_folder,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def delete_folder(request, name):
    """ Delete images folder """

    if not request.user.is_superuser:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text="This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    folder = get_object_or_404(ImagesFolder, name=name)
    folder.delete()
    sweetify.sweetalert(
        request, icon='success',
        title=f"Successfully deleted folder {folder.name}!")
    return redirect(reverse('view_all_folders'))
