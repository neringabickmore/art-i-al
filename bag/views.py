import sweetify

from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404
)

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ 
    Add the specified product 
    to the shopping bag 
    """

    product = get_object_or_404(Product, pk=product_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

       
    request.session['bag'] = bag
    if product_id in bag:
        sweetify.sweetalert(request, title='great news', icon='info', text= f'Artwork {product.name.upper()} is already in your bag!', timer=2000, timerProgressBar='true', persistent="Close")
    elif product_id not in bag:
        sweetify.sweetalert(request, title='success', icon='success', text= f'Added {product.name.upper()} to your bag.', timer=2000)
    else: 
        sweetify.sweetalert(request, title='warning', icon='warning', text= "Something went wrong. Let's take you to safety.", timer=2000, timerProgressBar='true', persistent="Close")
    bag[product_id] = quantity

    return redirect(redirect_url)


def remove_from_bag(request, product_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        
        bag = request.session.get('bag', {})
        bag.pop(product_id)
        sweetify.sweetalert(request, title='success', icon='success', text= f'Artwork {product.name.upper()} was removed from your bag.', timer=2000)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        sweetify.error(request, title='error', icon='error', text= f'Something went wrong removing {e}', timer=2000, timerProgressBar='true', persistent="Close")
        return HttpResponse(status=500)