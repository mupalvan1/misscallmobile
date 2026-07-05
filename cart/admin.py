from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    readonly_fields = ['price', 'created_at', 'updated_at']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'total_items', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['user__mobile', 'user__first_name', 'user__last_name']
    inlines = [CartItemInline]
    readonly_fields = ['created_at', 'updated_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity', 'price', 'total_price']
    list_filter = ['cart__is_active']
    search_fields = ['product__name', 'cart__user__mobile']
    readonly_fields = ['created_at', 'updated_at']