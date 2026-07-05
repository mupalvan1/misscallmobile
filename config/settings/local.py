"""
تنظیمات محیط توسعه (Local Settings)
این فایل فقط برای زمانی که روی سیستم خودت کد میزنی استفاده میشه.
"""

from .base import *

# حالت دیباگ (فقط در توسعه)
DEBUG = True

# اجازه دسترسی از همه هاست‌ها (فقط برای توسعه)
ALLOWED_HOSTS = ['*']

# ایمیل در کنسول چاپ بشه (برای تست)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'