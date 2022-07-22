from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, pin=None, password=None, **extra_fields):
        if not pin:
            raise ValueError('The given PIN must be set')
        user = self.model(pin=pin, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, pin, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(pin, password, **extra_fields)


class User(AbstractUser):

    username = None
    pin = models.CharField('ПИН', max_length=15, unique=True)
    first_name = models.CharField('Фамилия', max_length=150, blank=True)
    middle_name = models.CharField('Имя', max_length=100, blank=True)
    last_name = models.CharField('Отчество', max_length=100, blank=True, null=True)
    avatar = models.ImageField('Фото', upload_to='user_avatars/', null=True, blank=True)
    is_active = models.BooleanField('Работает', default=False)
    mobile = models.CharField("Телефон", max_length=10, null=True)

    USERNAME_FIELD = 'pin'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.middle_name}'
