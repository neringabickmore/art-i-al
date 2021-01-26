from django.urls import path
from . import views


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('shop/', views.shop, name='shop'),
]
