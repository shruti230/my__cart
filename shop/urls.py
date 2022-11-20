from django import views
from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name='shophome'),
   path("about/", views.aboutUs, name='aboutUs'),
   path("contact/", views.contactUs, name='ContactUs'),
   path("tracker/", views.tracker, name='tracker'),
   path("search/", views.search, name='Search'),
   path("products/<int:myid>", views.productView, name='productView'),
   path("checkout/", views.checkout, name='checkout')
] 