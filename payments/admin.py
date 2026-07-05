from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'order', 'amount', 'status', 
        'reference_id', 'authority', 'created_at'
    ]
    list_filter = ['status', 'created_at']
    search_fields = ['order__user__mobile', 'reference_id', 'authority']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('اطلاعات سفارش', {
            'fields': ('order', 'amount')
        }),
        ('وضعیت پرداخت', {
            'fields': ('status', 'reference_id', 'authority')
        }),
        ('اطلاعات کارت', {
            'fields': ('card_number',)
        }),
        ('تاریخ‌ها', {
            'fields': ('created_at', 'updated_at')
        }),
    )