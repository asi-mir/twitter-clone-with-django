from django.contrib import admin
from .models import User, Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

'''class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    
    fieldsets = (
        
    )'''

admin.site.register(User)
admin.site.register(Profile)
