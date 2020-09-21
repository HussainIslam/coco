from django import forms

from django_ace import AceWidget

from .models import Problem

class ProblemModelForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'language', 'status', 'difficulty', 'tags','description', 'code',]
        widgets = {
            "code": AceWidget(mode="python", theme="twilight"),
            'description': forms.Textarea(attrs={'id': 'textarea', 'novalidate': 'true'}),
        }
        