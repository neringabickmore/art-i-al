from django.contrib import admin
from .models import About, SocialMedia

class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'img',
        'url',
    )

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'icon',
        'url',
    )
    ordering = ('name',)

admin.site.register(About, AboutAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)