from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.review_add, name='review_add'),
    path('edit/', views.review_edit, name='review_edit'),
    path('delete/', views.review_delete, name='review_delete'),
]
