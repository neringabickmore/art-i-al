import sweetify

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

from .models import About, SocialMedia
from .forms import ContactForm
from .forms import AboutForm

from profiles.models import UserProfile
from products.models import Image


# Original code idea for sending mail: 
# https://github.com/irinatu17/Art-of-Tea/blob/master/contact/views.py
def index(request):
    """ 
    A view to return index page and render 
    contact form which sends a message to default 
    email address upon submission.
    """

    about_section = About.objects.all()
    social_icons = SocialMedia.objects.all()
    new_image = Image.objects.filter(show_in_new=True)
    gallery_image = Image.objects.filter(show_in_gallery=True)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            user_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    # captures user email in subject field
                    f"Message from {full_name}, <{user_email}>", 
                    message,
                    user_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                sweetify.sweetalert(request, icon='success',
                title= "Thank you! We have received your message!",
                text= "Please expect to hear from us within 72hours.",
                timer=2000, timerProgressBar='true', persistent="Close")
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        """
        Attempt to prefill full_name and email fields 
        for logged in user, if the info saved in their profile
        """
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            user_email = profile.user.email
            contact_form = ContactForm(initial={
                'full_name': profile.default_full_name,
                'email': profile.user.email,
                })
        else:
            contact_form = ContactForm()

    context = {
        'new_image': new_image,
        'gallery_image': gallery_image,
        'about_section': about_section,
        'contact_form': contact_form,
        'social_icons': social_icons,
    }

    return render(request, 'home/index.html', context)


@login_required
def edit_about(request, about_id):
    """ Edit about section  """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, title='error', icon='error',
            text= "This functionality is available to admin only.",
            timer=2000)
        return redirect(reverse('home'))

    about_section = get_object_or_404(About, pk=about_id)
    if request.method == 'POST':
        about_form = AboutForm(request.POST, instance=about_section)
        if about_form.is_valid():
            about_form.save()
            sweetify.sweetalert(request, icon='success',
                title= "Successfully updated about section!")
            return redirect(reverse('home'))
        else:
            sweetify.sweetalert(request, title='error', icon='error',
                text= "Failed to update about section. \
                     Please ensure the form is valid.",
                timer=2000, timerProgressBar='true', persistent="Close")
    else:
        about_form = AboutForm(instance=about_section)
        sweetify.sweetalert(request, icon='info',
                title= "You are editing about section")
    
    template = 'home/edit-about.html'
    context = {
        'about_form': about_form,
        'about_section': about_section,
    }

    return render(request, template, context)

