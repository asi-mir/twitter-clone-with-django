from django import forms
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **other_fields):
        if not phone:
            raise ValueError("Mobile is required")
        user = self.model(phone=phone, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('is_staff in admin must True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser in admin must True')
        return self.create_user(phone, password, **other_fields)


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=11, unique=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    token_expiration_date = models.DateTimeField(null=True)
    salt = models.CharField(max_length=32, null=True)
    object = UserManager()

    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = []

    backend = 'accounts.custombackend.PhoneBackend'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30, blank=False, default="")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, blank=True, default="")
    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('None', 'none'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    bio = models.TextField(max_length=150, null=True)
    profile_image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    birthdate = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    reported_times = models.PositiveIntegerField(blank=True, null=True)
    ACCOUNT_TYPE_CHOICES = (
        ('Paid', 'Paid'),
        ('Trial', 'Trial'),
    )
    account_type = models.CharField(max_length=6, choices=ACCOUNT_TYPE_CHOICES, default='')

    def __str__(self):
        return f'{self.user.phone}'

    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Field(models.Model):
    field = models.CharField(max_length=20)

    def __str__(self):
        return self.field


class Interest(models.Model):
    interest = models.CharField(max_length=20)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.interest
