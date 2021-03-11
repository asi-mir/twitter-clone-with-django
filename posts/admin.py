from django.contrib import admin

from .models import Files, Post

admin.site.register(Post)
admin.site.register(Files)

