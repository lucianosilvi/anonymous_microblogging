from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['name', 'message']

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) > 50:
            raise forms.ValidationError("Message is longer than allowed")
        return message
