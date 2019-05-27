from django import forms
from django.core.validators import validate_email
from django.contrib.auth.models import User
from myshop.models import Profile

class Userform(forms.ModelForm):
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

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.isdigit():
            raise forms.ValidationError("user must contain atleast a character")

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            verify = validate_email(email)
        except:
            raise forms.ValidationError("Email is not Valid")
        return email

    def clean_confirm_password(self):

        password = self.cleaned_data.get('password')

        confirm_password = self.cleaned_data.get('confirm_password')

        if (password != confirm_password):

            raise forms.ValidationError("confirm password is not matched ")

        return password

class Profileform(forms.ModelForm):
    mobile_number=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number '}),
                        required=True)
    class Meta():
        model=Profile
        fields=['mobile_number']

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        length = len(str(mobile_number))
        if (length > 10 or length < 10):
            raise forms.ValidationError("mobile number must be of 10 digit")
        return mobile_number

