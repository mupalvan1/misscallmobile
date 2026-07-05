from django.db import models
from django.conf import settings
from orders.models import Order

class Payment(models.Model):
    """
    مدل پرداخت
    """
    STATUS_CHOICES = (
        ('pending', 'در انتظار پرداخت'),
        ('paid', 'پرداخت شده'),
        ('failed', 'پرداخت ناموفق'),
        ('refunded', 'بازگشت وجه'),
    )
    
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='سفارش'
    )
    amount = models.DecimalField(
        max_digits=12, 
        decimal_places=0, 
        verbose_name='مبلغ پرداختی (تومان)'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='وضعیت'
    )
    reference_id = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='کد مرجع'
    )
    authority = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='کد مجوز'
    )
    card_number = models.CharField(
        max_length=16, 
        blank=True, 
        null=True, 
        verbose_name='شماره کارت'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت‌ها'
        ordering = ['-created_at']

    def __str__(self):
        return f"پرداخت #{self.id} - سفارش #{self.order.id}"

    def mark_as_paid(self):
        """تغییر وضعیت به پرداخت شده"""
        self.status = 'paid'
        self.save()
        # به‌روزرسانی وضعیت سفارش
        self.order.status = 'paid'
        self.order.save()

    def mark_as_failed(self):
        """تغییر وضعیت به پرداخت ناموفق"""
        self.status = 'failed'
        self.save()
        # به‌روزرسانی وضعیت سفارش
        self.order.status = 'pending'
        self.order.save()