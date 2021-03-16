from django.contrib import admin

from .models import Profile, User, Field, Interest

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Field)
admin.site.register(Interest)
