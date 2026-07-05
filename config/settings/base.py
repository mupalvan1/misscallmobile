"""
تنظیمات پایه (Base Settings)
این فایل شامل تنظیمات مشترک بین همه محیط‌هاست.
یعنی تنظیماتی که در توسعه و تولید یکسان هستند.
"""

from pathlib import Path
import os


# مسیر ریشه پروژه (همون پوشه اصلی)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# کلید مخفی جنگو (از محیط خوانده میشه)
SECRET_KEY = 'django-insecure-temp-key-change-in-production'

# برنامه‌های نصب شده
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'products',
]

# میان‌افزارها (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# فایل اصلی URL ها
ROOT_URLCONF = 'config.urls'

# تنظیمات قالب‌ها (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# نقطه ورود WSGI (برای سرورهای معمولی)
WSGI_APPLICATION = 'config.wsgi.application'

# دیتابیس (پیش‌فرض SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# اعتبارسنجی رمز عبور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# زبان و منطقه زمانی
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# فایل‌های استاتیک (CSS, JS, تصاویر)
STATIC_URL = 'static/'

# فیلد پیش‌فرض برای کلید اصلی
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# مدل کاربر سفارشی
AUTH_USER_MODEL = 'accounts.User'