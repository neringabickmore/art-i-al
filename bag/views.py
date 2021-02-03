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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[product_id] = quantity
    
    request.session['bag'] = bag
    print(request.session['bag'])
    
    return redirect(redirect_url)