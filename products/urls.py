from django.urls import path
from . import views


urlpatterns = [
    path(
        'gallery/', views.gallery, name='gallery'),
    path('shop/', views.shop, name='shop'),
    path(
        '<name>/', views.product_detail, name='product_detail'),
    # Product management options
    path(
        'manage/product/', views.product_management,
        name='product_management'),
    # Collections management
    path(
        'view/all/collections/', views.view_all_collections,
        name='view_all_collections'),
    path(
        'add/collection/', views.add_collection,
        name='add_collection'),
    path(
        'edit/collection/<int:collection_id>/', views.edit_collection,
        name='edit_collection'),
    path(
        'delete/collection/<name>/', views.delete_collection,
        name='delete_collection'),
    # Images management
    path(
        'view/all/images/', views.view_all_images,
        name='view_all_images'),
    path(
        'add/image/', views.add_img, name='add_img'),
    path(
        'edit/image/<int:image_id>/', views.edit_img,
        name='edit_img'),
    path(
        'delete/img/<name>/', views.delete_image,
        name='delete_image'),
    # Images Folder management
    path(
        'view/all/folders/', views.view_all_folders,
        name='view_all_folders'),
    path(
        'add/images/folder/', views.add_img_folder,
        name='add_img_folder'),
    path(
        'edit/images/folder/<int:folder_id>/', views.edit_img_folder,
        name='edit_img_folder'),
    path(
        'delete/img/folder/<name>/', views.delete_folder,
        name='delete_folder'),
    # Product Management
    path(
        'add/product/', views.add_product,
        name='add_product'),
    path(
        'edit/product/<int:product_id>/', views.edit_product,
        name='edit_product'),
    path(
        'delete/product/<name>/', views.delete_product,
        name='delete_product'),
]
