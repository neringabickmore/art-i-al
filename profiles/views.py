import sweetify
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from home.models import SocialMedia


@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)
    social_media = SocialMedia.objects.all()

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, instance=profile)
        if form.is_valid():
            form.save()
            sweetify.sweetalert(
                request, title='success', icon='success',
                text=f'Profile updated successfully.',
                timer=2000)
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="Update failed. Please ensure the form is valid",
                timer=2000)
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all().order_by('-purchase_date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'all_social_media': social_media,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ User order history """

    order = get_object_or_404(Order, order_number=order_number)
    social_media = SocialMedia.objects.all()

    sweetify.sweetalert(
        request, title='info', icon='info',
        text=f'This is a past confirmation for order number {order_number}.\
        A confirmation email was sent on the order date.',
        timer=2000)

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
        'from_profile': True,
        'all_social_media': social_media,
    }

    return render(request, template, context)
