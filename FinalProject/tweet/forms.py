from django import forms
from .models import tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['text', 'photo']