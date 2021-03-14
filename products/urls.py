from django.urls import path
from . import views


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('shop/', views.shop, name='shop'),
    path('<name>/', views.product_detail, name='product_detail'), 
    path('add/collection/', views.add_collection, name='add_collection'),
    path('edit/collection/<name>/', views.edit_collection, name='edit_collection'),
    path('add/image/', views.add_img, name='add_img'),
    path('edit/image/<name>/', views.edit_img, name='edit_img'),
    path('add/images/folder/', views.add_img_folder, name='add_img_folder'),
    path('add/product/', views.add_product, name='add_product'),
]
