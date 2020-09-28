from django import forms

from .models import Problem

class ProblemModelForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'language', 'status', 'difficulty', 'tags','description', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'language': forms.Select(attrs={'class': 'custom-select col-sm-2'}),
            'status': forms.Select(attrs={'class': 'custom-select col-sm-2'}),
            'difficulty': forms.Select(attrs={'class': 'custom-select col-sm-2'}),
            'tags': forms.TextInput(attrs={'class': 'form-control col-sm-2', "placeholder": 'comma-seperated tags'}),
            'description': forms.Textarea(attrs={'id': 'textarea', 'novalidate': 'true'}),
        }
        