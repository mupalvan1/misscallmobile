from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    """
    مدل سفارش
    """
    STATUS_CHOICES = (
        ('pending', 'در انتظار پرداخت'),
        ('paid', 'پرداخت شده'),
        ('shipped', 'ارسال شده'),
        ('delivered', 'تحویل داده شده'),
        ('cancelled', 'لغو شده'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='کاربر'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='وضعیت'
    )
    total_price = models.DecimalField(
        max_digits=12, 
        decimal_places=0, 
        verbose_name='قیمت کل (تومان)'
    )
    shipping_address = models.TextField(verbose_name='آدرس تحویل')
    shipping_cost = models.DecimalField(
        max_digits=12, 
        decimal_places=0, 
        default=0,
        verbose_name='هزینه ارسال'
    )
    discount = models.DecimalField(
        max_digits=12, 
        decimal_places=0, 
        default=0,
        verbose_name='تخفیف'
    )
    tracking_code = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='کد رهگیری'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
        ordering = ['-created_at']

    def __str__(self):
        return f"سفارش #{self.id} - {self.user.mobile}"

    @property
    def final_price(self):
        """قیمت نهایی با احتساب تخفیف و هزینه ارسال"""
        return self.total_price + self.shipping_cost - self.discount


class OrderItem(models.Model):
    """
    مدل آیتم‌های سفارش
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='سفارش'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name='محصول'
    )
    quantity = models.PositiveIntegerField(verbose_name='تعداد')
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='قیمت (تومان)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'آیتم سفارش'
        verbose_name_plural = 'آیتم‌های سفارش'

    def __str__(self):
        return f"{self.product.name} - {self.quantity} عدد"

    @property
    def total_price(self):
        """قیمت کل این آیتم"""
        return self.price * self.quantity