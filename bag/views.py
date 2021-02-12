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

    bag[product_id] = quantity
    
    request.session['bag'] = bag
    sweetify.sweetalert(request, title='Success', icon='success', text="You have added item to the bag", timer=5000, timerProgressBar='true', persistent="Close")
    
    return redirect(redirect_url)


def remove_from_bag(request, product_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        
        bag = request.session.get('bag', {})
        bag.pop(product_id)
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)