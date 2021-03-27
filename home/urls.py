from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    # About section management
    path('edit/about/<int:about_id>/', views.edit_about, name='edit_about'),
    # Social media management
    path('social-media/', views.social_media, name='social_media'),
    
]

