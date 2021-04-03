import sweetify
import stripe
import json

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from home.models import SocialMedia
from bag.contexts import bag_contents

from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse


@require_POST
def cache_checkout_data(request):
    """
    Caches data in the checkout.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        sweetify.sweetalert(
            request, title='error', icon='error',
            text='Sorry, your payment cannot be \
            processed right now. Please try again later.',
            timer=2000, timerProgressBar='true', persistent="Close")
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Checkout view to process the order
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    social_media = SocialMedia.objects.all()
    product = Product.objects.all()

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        """
        Checks if items are still available for sale
        if not, pops items that are sold.
        """
        for product_id, item_data in bag.items():
            product = Product.objects.get(id=product_id)
            if product.is_sold:
                sweetify.sweetalert(
                    request, title='info', icon='info',
                    text="Oh no, somebody bought your item a moment ago. \
                    Please check the shop for alternatives or contact us.",
                    timer=2000, timerProgressBar='true',
                    persistent="close")
                bag.pop(product_id)
                request.session['bag'] = bag
                if not bag.items():
                    return redirect(reverse('shop'))
                else:
                    sweetify.sweetalert(
                        request, title='info', icon='info',
                        text="Oh no, somebody bought one of your items. \
                        Continue to checkout or see for more items \
                        in the shop.",
                        timer=2000, timerProgressBar='true',
                        persistent="Close")
                    return redirect(reverse('checkout'))

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # prevents multiple saves with commit=False
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for product_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=product_id)
                    # switches item to sold.
                    product.is_sold = True
                    product.save()
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    sweetify.sweetalert(
                        request, title='error', icon='error',
                        text="One of the products in your bag \
                        wasn't found in our database. "
                        "Please call us for assistance!",
                        timer=2000, timerProgressBar='true',
                        persistent="close")
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse(
                    'checkout_success',
                    args=[order.order_number]))
        else:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text='There was an error with your form. \
                Please double check your information.',
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        bag = request.session.get('bag', {})
        if not bag:
            sweetify.sweetalert(
                request, title='error', icon='error',
                text="There's nothing in your bag at the moment",
                timer=2000, timerProgressBar='true', persistent="Close")
            return redirect(reverse('shop'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
        )

        """
        Attempt to prefill the form with any
        info the user maintains in their profile
        """
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            sweetify.sweetalert(
                request, title='warning', icon='warning',
                text="Stripe public key is missing. \
                Did you forget to set it in your environment?",
                timer=2000, timerProgressBar='true', persistent="Close")

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret':  intent.client_secret,
            'all_social_media': social_media,
        }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    social_media = SocialMedia.objects.all()

    # Only if the user is authenticated save the info to their profile
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(
                profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    sweetify.sweetalert(
        request, title='success', icon='success',
        text=f'Order successfully processed! \
        A confirmation email will be sent to {order.email}.',
        timer=2000)

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
        'all_social_media': social_media,
    }

    return render(request, template, context)

@login_required
def all_orders_history(request):
    """ A view that renders all historical orders """

    orders = Order.objects.all().order_by('purchase_date')
    product = Product.objects.all()
    line_item = OrderLineItem.objects.all()
    social_media = SocialMedia.objects.all()

    template = 'checkout/all-orders-history.html'

    context = {
        'all_social_media': social_media,
        'orders': orders,
        'line_item': line_item,
        'product' : product,
    }

    return render(request, template, context)
