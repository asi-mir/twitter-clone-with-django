from django import forms

from .models import Post


class TweetForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
