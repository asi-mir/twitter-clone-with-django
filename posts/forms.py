from django.forms import ClearableFileInput
from django import forms

from posts.models import Post, Files


class FeedModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']


class FileModelForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }
