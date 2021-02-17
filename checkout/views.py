import sweetify

from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        sweetify.error(request, title='error', icon='error',
        text= "There's nothing in your bag at the moment",
        timer=2000, timerProgressBar='true', persistent="Close")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
