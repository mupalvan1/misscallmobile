from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    """
    مدل سبد خرید
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='کاربر'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید'
        ordering = ['-created_at']

    def __str__(self):
        return f"سبد خرید {self.user.mobile} - {self.created_at}"

    @property
    def total_price(self):
        """محاسبه قیمت کل سبد خرید"""
        total = sum(item.total_price for item in self.items.all())
        return total

    @property
    def total_items(self):
        """تعداد کل آیتم‌های سبد خرید"""
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    """
    مدل آیتم‌های سبد خرید
    """
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='سبد خرید'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='محصول'
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='قیمت (تومان)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'آیتم سبد خرید'
        verbose_name_plural = 'آیتم‌های سبد خرید'
        unique_together = ['cart', 'product']

    def __str__(self):
        return f"{self.product.name} - {self.quantity} عدد"

    @property
    def total_price(self):
        """قیمت کل این آیتم"""
        return self.price * self.quantity