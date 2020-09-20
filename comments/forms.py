from django import forms

from martor.fields import MartorFormField

from .models import Comment

class CommentForm(forms.ModelForm):
    body = MartorFormField()
    class Meta:
        model = Comment
        fields = ('body',)