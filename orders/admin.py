from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ['price', 'created_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'status', 'total_price', 'final_price',
        'shipping_address', 'tracking_code', 'created_at'
    ]
    list_filter = ['status', 'created_at']
    search_fields = ['user__mobile', 'user__first_name', 'user__last_name', 'tracking_code']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('اطلاعات کاربر', {
            'fields': ('user', 'shipping_address')
        }),
        ('اطلاعات مالی', {
            'fields': ('total_price', 'shipping_cost', 'discount')
        }),
        ('وضعیت سفارش', {
            'fields': ('status', 'tracking_code')
        }),
        ('تاریخ‌ها', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity', 'price', 'total_price']
    list_filter = ['order__status']
    search_fields = ['product__name', 'order__user__mobile']
    readonly_fields = ['created_at']