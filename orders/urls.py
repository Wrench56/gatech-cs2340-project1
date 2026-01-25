from django.urls import path

from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('add/', views.order_add, name='orders_add'),
]
