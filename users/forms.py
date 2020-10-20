from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from datetime import datetime

from .models import CustomUser, ProgrammingLanguage


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password', 
                'class': 'form-control'
            }
        ),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control'
            }
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email',
                  'avatar', 'profile', 'dob', 'languages',]
        current_year = datetime.now().year
        list_of_years = range(current_year - 99, current_year + 1)[::-1]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'profile': forms.Textarea(attrs={'class': 'form-control'}),
            'dob': forms.SelectDateWidget(years=list_of_years),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        current_year = datetime.now().year
        list_of_years = range(current_year - 99, current_year + 1)[::-1]
        fields = ('username', 'first_name', 'last_name', 'email',
                  'avatar', 'profile', 'dob', 'password')
        #fields = '__all__'
        widgets = {
            'dob': forms.SelectDateWidget(years=list_of_years)
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
                'class': 'form-control', 
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(label="Password",strip=False,widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password', 
                'placeholder': 'Password'
            }
        ),
    )


class ProgrammingLanguageForm(ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name', 'abbreviation']
