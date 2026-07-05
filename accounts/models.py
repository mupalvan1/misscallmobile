from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    """
    مدیریت کاربر سفارشی برای حذف username
    """
    def create_user(self, mobile, first_name, last_name, password=None, **extra_fields):
        if not mobile:
            raise ValueError('شماره موبایل اجباری است')
        if not first_name:
            raise ValueError('نام اجباری است')
        if not last_name:
            raise ValueError('نام خانوادگی اجباری است')
        
        user = self.model(
            mobile=mobile,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, mobile, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(mobile, first_name, last_name, password, **extra_fields)

class User(AbstractUser):
    """
    مدل کاربر سفارشی با شماره موبایل
    """
    # حذف فیلد username
    username = None
    
    # شماره موبایل به عنوان شناسه اصلی
    mobile = models.CharField(
        max_length=11, 
        unique=True,
        verbose_name='شماره موبایل'
    )
    
    # فیلدهای اضافی
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    
    # تعیین فیلد اصلی برای احراز هویت
    USERNAME_FIELD = 'mobile'
    
    # فیلدهای مورد نیاز برای createsuperuser
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    # استفاده از UserManager سفارشی
    objects = UserManager()
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    
    def __str__(self):
        return self.mobile
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"