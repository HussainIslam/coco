from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, ProgrammingLanguage

class CustomUserCreationForm(UserCreationForm):
    
    class Meta: 
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('avatar', 'profile', 'dob',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'profile', 'dob',)

class ProgrammingLanguageForm(ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name','abbreviation']