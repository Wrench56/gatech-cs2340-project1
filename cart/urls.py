from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('remove/', views.cart_remove, name='cart_remove'),
    path('add/', views.cart_add, name='cart_add'),
]
