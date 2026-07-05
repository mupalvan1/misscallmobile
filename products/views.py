from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    """
    نمایش لیست همه محصولات
    """
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories
    })

def product_detail(request, slug):
    """
    نمایش جزئیات یک محصول
    """
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'products/product_detail.html', {
        'product': product
    })

def category_products(request, slug):
    """
    نمایش محصولات یک دسته‌بندی
    """
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(is_active=True)
    return render(request, 'products/category_products.html', {
        'category': category,
        'products': products
    })