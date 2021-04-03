from django.contrib import admin
from .models import Product, Category, Collection, Image, ImagesFolder, Tag


class ProductAdmin(admin.ModelAdmin):
    """
    Poduct management in admin.
    """

    list_display = (
        'name',
        'category',
        'collection_name',
        'description',
        'author',
        'dimensions',
        'price',
        'images_folder',
        'sku',
        'tag',
        'is_sold',
    )

    ordering = ['collection_name']


class CategoryAdmin(admin.ModelAdmin):
    """
    Poduct category management in admin.
    """

    list_display = (
        'friendly_name',
        'name',
    )


class CollectionAdmin(admin.ModelAdmin):
    """
    Poduct collection management in admin.
    """

    list_display = (
        'friendly_name',
        'name',
    )


class TagAdmin(admin.ModelAdmin):
    """
    Poduct tag management in admin.
    """

    list_display = (
        'friendly_name',
        'name',
    )


class ImageAdmin(admin.ModelAdmin):
    """
    Image management in admin.
    """

    list_display = (
        'name',
        'img',
        'url',
        'main_img',
        'room_view',
    )

    ordering = ('name',)


class ImagesFolderAdmin(admin.ModelAdmin):
    """
    Images folder management in admin.
    """

    display = 'name'
    filter_horizontal = ('imgs',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImagesFolder, ImagesFolderAdmin)
admin.site.register(Tag, TagAdmin)
