from django.urls import path
from . import views


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('shop/', views.shop, name='shop'),
    path('<int:product_id>/', views.product_detail, name='product_detail'), 
    path('products/add-product/', views.add_product, name='add_product'),
]
