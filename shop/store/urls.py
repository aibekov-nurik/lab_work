from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products_view'),
    path('products/', views.products_view, name='products_view'),
    path('products/<int:id>/', views.product_view, name='product_view'),
    path('products/edit/<int:id>/', views.product_edit_view, name='product_edit_view'),
    path('products/delete/<int:id>/', views.product_delete_view, name='product_delete_view'),
    path('categories/add/', views.category_add_view, name='category_add_view'),
    path('products/add/', views.product_add_view, name='product_add_view'),
]

