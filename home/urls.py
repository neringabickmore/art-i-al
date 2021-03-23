from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('edit/about/<int:about_id>/', views.edit_about, name='edit_about'),
]
