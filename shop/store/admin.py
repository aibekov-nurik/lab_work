from django.contrib import admin
from .models import Category, Product, OrderItem, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('username', 'phone')
    inlines = [OrderItemInline]
    ordering = ['-created_at']
