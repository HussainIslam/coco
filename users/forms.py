from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, ProgrammingLanguage

class CustomUserCreationForm(UserCreationForm):
    
    class Meta: 
        model = get_user_model()
        fields = ( 'username', 'first_name', 'last_name', 'email', 'avatar', 'profile', 'dob', 'languages',)
        list_of_years = range(1950, 2020)
        widgets = {
            'dob': forms.SelectDateWidget(years=list_of_years)
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        list_of_years = range(1950, 2020)
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar', 'profile', 'dob', 'password')
        #fields = '__all__'
        widgets = {
            'dob': forms.SelectDateWidget(years=list_of_years)
        }

class ProgrammingLanguageForm(ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name','abbreviation']