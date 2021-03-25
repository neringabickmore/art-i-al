import sweetify

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import About, SocialMedia
from .forms import AboutForm

from products.models import Image


def index(request):
    """ A view to return index page """

    about_section = About.objects.all()
    social_icons = SocialMedia.objects.all()
    new_image = Image.objects.filter(show_in_new=True)
    gallery_image = Image.objects.filter(show_in_gallery=True)

    context = {
        'about_section': about_section,
        'social_icons': social_icons,
        'new_image': new_image,
        'gallery_image': gallery_image,
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

