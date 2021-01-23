from django.contrib import admin
from .models import Product, Category, Collection, Image, ImagesFolder, Tag

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'collection_name',
        'description',
        'author',
        'dimensions',
        'price',
        'images_folder',
        'sku',
        'tag',
        'ft_new',
        'ft_preview',
    )

    ordering = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'img',
        'image_url',
    )

    ordering = ('name',)


class ImagesFolderAdmin(admin.ModelAdmin):
    filter_horizontal = ('imgs',)
    display = 'name'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImagesFolder, ImagesFolderAdmin)
admin.site.register(Tag, TagAdmin)