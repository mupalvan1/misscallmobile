"""
تنظیمات محیط تولید (Production Settings)
این فایل برای زمانی که سایت روی سرور اصلی اجرا میشه.
"""

from .base import *

# حالت دیباگ خاموش (امنیت بالاتر)
DEBUG = False

# فقط دامنه‌های مجاز (باید بعداً تغییر کنه)
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# تنظیمات امنیتی برای HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True