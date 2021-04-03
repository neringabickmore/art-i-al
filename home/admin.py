from django.contrib import admin
from .models import About, SocialMedia


class AboutAdmin(admin.ModelAdmin):
    """
    About section admin
    """

    list_display = (
        'name',
        'description',
    )


class SocialMediaAdmin(admin.ModelAdmin):
    """
    Social Media Admin
    """

    list_display = (
        'name',
        'icon',
        'url',
    )
    ordering = ('name',)

admin.site.register(About, AboutAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
