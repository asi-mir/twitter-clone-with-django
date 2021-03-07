from .models import Post
from django import forms

class TweetForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']