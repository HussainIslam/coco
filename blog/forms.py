from django import forms

from martor.fields import MartorFormField

from .models import Blog

class BlogModelForm(forms.ModelForm):
    body = MartorFormField()
    class Meta:
        model = Blog
        fields = ('title','status', 'blog_tags', 'body', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'status': forms.Select(attrs={'class': 'custom-select col-sm-2'}),
            'blog_tags': forms.TextInput(attrs={ 'class': 'form-control col-sm-9' })
        }