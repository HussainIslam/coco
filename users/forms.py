from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, ProgrammingLanguage

class CustomUserCreationForm(UserCreationForm):
    
    class Meta: 
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email','avatar', 'profile', 'dob', 'languages',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        #fields = ('username', 'email', 'avatar', 'profile', 'dob',)
        fields = '__all__'

class ProgrammingLanguageForm(ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name','abbreviation']