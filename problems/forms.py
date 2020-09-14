from django import forms

from django_ace import AceWidget

from .models import Problem

class ProblemModelForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'language', 'status','description', 'code',]
        widgets = {
            "code": AceWidget(mode="python", theme="twilight"),
        }
        