from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

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
        return self.create_user(phone,password,**other_fields)



class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=11, unique=True)
    token = models.PositiveIntegerField(blank=True, null=True)
    token_date = models.DateTimeField(auto_now=True)

    object = UserManager()

    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = []

    backend = 'accounts.custombackend.PhoneBackend'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    #image = models.ImageField(upload_to = 'profile_pics')
    # Add more fields

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