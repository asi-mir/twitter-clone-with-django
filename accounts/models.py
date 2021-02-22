from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField(blank=True, null=True)
#     phone = models.CharField(max_length = 20)
#     bio = models.TextField(blank=True, null=True)
