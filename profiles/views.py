import sweetify
from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            sweetify.sweetalert(request, title='success', icon='success',
            text= f'Profile updated successfully.',
            timer=2000)
        else:
            sweetify.sweetalert(request, title='error', icon='error',
            text= "Update failed. Please ensure the form is valid",
            timer=2000)
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    sweetify.sweetalert(request, title='info', icon='info',
            text= f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.',
            timer=2000)

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)