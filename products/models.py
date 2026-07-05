from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """
    دسته‌بندی محصولات
    """
    name = models.CharField(max_length=100, verbose_name='نام دسته')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        verbose_name='دسته والد'
    )
    description = models.TextField(blank=True, verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """
    مدل محصولات
    """
    name = models.CharField(max_length=200, verbose_name='نام محصول')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='دسته‌بندی'
    )
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='قیمت (تومان)')
    discount_price = models.DecimalField(
        max_digits=12, 
        decimal_places=0, 
        blank=True, 
        null=True, 
        verbose_name='قیمت با تخفیف'
    )
    stock = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_featured = models.BooleanField(default=False, verbose_name='ویژه')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def final_price(self):
        """قیمت نهایی با احتساب تخفیف"""
        if self.discount_price and self.discount_price < self.price:
            return self.discount_price
        return self.price


class ProductImage(models.Model):
    """
    تصاویر اضافی محصول
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='محصول'
    )
    image = models.ImageField(upload_to='products/gallery/', verbose_name='تصویر')
    is_main = models.BooleanField(default=False, verbose_name='تصویر اصلی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصولات'

    def __str__(self):
        return f"{self.product.name} - {self.id}"