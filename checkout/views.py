import sweetify

from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        sweetify.sweetalert(request, title='error', icon='error',
        text= "There's nothing in your bag at the moment",
        timer=2000, timerProgressBar='true', persistent="Close")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HzqGcGCLUu8fSM59I2dn2X6NMrmmT17v5jPgQ9dnsVj75H2hGe16wGKawMHT4aBOAtH14BdJ7DVIKjPW1Dx2ODv006ZSV8Vmg',
        'client_secret':  'test client secret',
    }

    return render(request, template, context)
