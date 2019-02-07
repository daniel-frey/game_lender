from django import forms

from .models import Message


class MessageForm(forms.Form):

    class Meta:
        model = Message
        fields = [
            'to_user',
            'subject',
            'body'
        ]

    to_user = forms.CharField(label='To', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
