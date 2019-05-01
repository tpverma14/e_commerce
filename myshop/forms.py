from django import forms
from django.contrib.auth.models import User


class Userform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter UserName'}),
                               required=True, max_length=30)

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
                            required=True, max_length=30)

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}), required=True,
        max_length=30)

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}), required=True,
        max_length=30)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), required=True,
        max_length=30)

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), required=True,
        max_length=30)
    class meta():
            model=User
            field=['username','email','first_name','last_name','password ','confirm_password']