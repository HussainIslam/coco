from django import forms

from martor.fields import MartorFormField

from .models import Comment, BlogComment

class CommentForm(forms.ModelForm):
    body = MartorFormField()
    class Meta:
        model = Comment
        fields = ('body',)

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('body',)