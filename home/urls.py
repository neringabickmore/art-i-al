from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    # About section management
    path('edit/about/<int:about_id>/', views.edit_about, name='edit_about'),
    # Social media management
    path(
        'social-media/', views.social_media,
        name='social_media'),
    path(
        'add/social-media/', views.add_social_media,
        name='add_social_media'),
    path(
        'edit/social-media/<int:social_media_id>/',
        views.edit_social_media, name='edit_social_media'),
    path(
        'remove/social-media/<int:social_media_id>/',
        views.remove_social_media, name='remove_social_media'),
]
