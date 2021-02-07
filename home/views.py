from django.shortcuts import render
from .models import About, SocialMedia

from products.models import Image


def index(request):
    """ A view to return index page """

    about = About.objects.all()
    social_icons = SocialMedia.objects.all()
    new_image = Image.objects.filter(show_in_new=True)
    gallery_image = Image.objects.filter(show_in_gallery=True)

    context = {
        'about': about,
        'social_icons': social_icons,
        'new_image': new_image,
        'gallery_image': gallery_image,
    }
    
    return render(request, 'home/index.html', context)

