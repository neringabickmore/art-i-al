from django.urls import path
from . import views


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('shop/', views.shop, name='shop'),
    path('<name>/', views.product_detail, name='product_detail'), 
    path('add/product/', views.add_product, name='add_product'),
    path('add/collection/', views.add_collection, name='add_collection'),
    path('add/images/folder/', views.add_img_folder, name='add_img_folder'),
]
