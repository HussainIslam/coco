from django import forms

from .models import Problem

class ProblemModelForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'language', 'status', 'difficulty', 'tags','description', ]
        widgets = {
            'description': forms.Textarea(attrs={'id': 'textarea', 'novalidate': 'true'}),
        }
        