from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('info.html/', views.info, name = "info"),
    path('products.html/', views.products, name = 'products'),
    path('about.html/', views.About_Us, name = 'about_us'),
    path('contact.html/', views.contact_Us, name = 'Contact_us'),
    path('gallery.html/', views.gallery, name = 'gallery'),
]