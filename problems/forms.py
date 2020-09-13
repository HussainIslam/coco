from django.forms import ModelForm

from .models import Problem

class ProblemModelForm(ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'language', 'status', 'body',]
        