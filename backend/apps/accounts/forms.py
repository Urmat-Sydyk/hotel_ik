from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

from backend.apps.accounts.models import User


class LoginForm(forms.Form):
    pin = forms.CharField(
        validators=[validators.MaxLengthValidator(14), validators.MinLengthValidator(14)],
        label='пин',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ПИН'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "autocomplete": "off",
                "placeholder": "Пароль"
            }
        )
    )


class UserRegisterForm(UserCreationForm):
    pin = forms.CharField(
        validators=[validators.MaxLengthValidator(14), validators.MinLengthValidator(14)],
        label='ПИН',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите свой ПИН'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Придумайте пароль'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Введите пароль повторно'})
    )

    class Meta:
        model = User
        fields = [
            'pin',
            'first_name',
            'middle_name',
            'last_name',
            'mobile',
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите свою фамилию'}),
            "middle_name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите свое имя'}),
            "last_name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите свое отчество'}),
            "mobile": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите свой номер телефона'}),

        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'avatar',
            'first_name',
            'middle_name',
            'last_name',
            'mobile',
        ]
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
        }
