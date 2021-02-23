from django import forms
from django.db.models import fields

from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields=['content']

#    def clean_content(): to have at least a hashtag
