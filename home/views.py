from django.shortcuts import render
from products.models import Product, Category

def home(request):
    """
    صفحه اصلی سایت
    """
    # محصولات ویژه
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    
    # جدیدترین محصولات
    latest_products = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    
    # دسته‌بندی‌ها
    categories = Category.objects.all()
    
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
        'categories': categories,
    }
    return render(request, 'home/home.html', context)