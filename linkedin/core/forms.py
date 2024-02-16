from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


def validate_no_numbers(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError(
            'Name and job title should not contain numbers.')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['job_title']

    job_title = forms.CharField(
        max_length=255,
        validators=[validate_no_numbers],
        widget=forms.TextInput(attrs={'placeholder': 'Your job title'}),
        error_messages={
            'min_length': 'Job title should be at least 14 characters long.'}
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    job_title = forms.CharField(max_length=255, required=True,
                                help_text='Required. Should be at least 14 characters long.',
                                validators=[validate_no_numbers],
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Your job title'}),
                                error_messages={
                                    'min_length': 'Job title should be at least 14 characters long.'
                                })

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'job_title')

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Your username',
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={'placeholder': 'Your first name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Your last name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address', 'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'placeholder': 'Your job title', 'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Your username', 'class': 'form-control'}),
        error_messages={'required': 'Please enter your username.'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Your password', 'class': 'form-control'}),
        error_messages={'required': 'Please enter your password.'}
    )
