from django.urls import path
from . import views


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('shop/', views.shop, name='shop'),
    path('<name>/', views.product_detail, name='product_detail'), 
    # Collections management
    path('add/collection/', views.add_collection, name='add_collection'),
    path('edit/collection/<name>/', views.edit_collection, name='edit_collection'),
    # Images management
    path('add/image/', views.add_img, name='add_img'),
    path('edit/image/<name>/', views.edit_img, name='edit_img'),
    # Images Folder management
    path('add/images/folder/', views.add_img_folder, name='add_img_folder'),
    path('edit/images/folder/<name>', views.edit_img_folder, name='edit_img_folder'),
    # Product Management
    path('add/product/', views.add_product, name='add_product'),
    path('edit/product/<name>', views.edit_product, name='edit_product'),
]
