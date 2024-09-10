from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)
    
    def save(self, phone_number, password=None, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

# Custom User Model
class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.png')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()


    def __str__(self):
        return self.full_name

    def get_full_name(self):
        return self.full_name

    def get_profile_picture(self):
        return self.profile_picture.url

    def get_role(self):
        return self.account.role

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number   


# Account Model
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('employee', 'Employee'),
        ('manager', 'Manager'),
        ('boss', 'Boss'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.full_name
    
    def get_role(self):
        return self.role
    


