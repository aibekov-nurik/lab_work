from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView, CategoryCreateView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='products_view'),
    path('products/', ProductListView.as_view(), name='products_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('products/add/', ProductCreateView.as_view(), name='product_add_view'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit_view'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add_view'),
]
