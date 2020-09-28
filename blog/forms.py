from django import forms

from martor.fields import MartorFormField

from .models import Blog

class BlogModelForm(forms.ModelForm):
    body = MartorFormField()
    class Meta:
        model = Blog
        fields = ('title','status', 'blog_tags', 'body', )
        #fields = '__all__'