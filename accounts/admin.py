from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    نمایش کاربران در پنل ادمین
    """
    # فیلدهایی که در لیست نمایش داده میشن
    list_display = ['mobile', 'first_name', 'last_name', 'is_active', 'is_staff']
    
    # فیلدهای جستجو
    search_fields = ['mobile', 'first_name', 'last_name']
    
    # فیلترها
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    
    # ترتیب نمایش
    ordering = ['-date_joined']
    
    # فیلدهایی که در صفحه ویرایش نمایش داده میشن
    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': ('mobile', 'first_name', 'last_name', 'email', 'password')
        }),
        ('دسترسی‌ها', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('تاریخ‌ها', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    # فیلدهایی که در صفحه ایجاد کاربر نمایش داده میشن
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )