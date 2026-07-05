from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # صفحه اصلی (home)
    path('products/', include('products.urls')),  # محصولات
    path('cart/', include('cart.urls')),  # سبد خرید
    path('orders/', include('orders.urls')),  # سفارشات
    path('payments/', include('payments.urls')),  # پرداخت
    path('accounts/', include('accounts.urls')),  # کاربران
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)