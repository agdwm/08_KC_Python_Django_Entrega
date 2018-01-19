import self as self
from django import forms


class LoginForm(forms.Form):

    login_username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label="Username",
        error_messages={'required': 'Este campo es obligatorio'}
    )
    login_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Password",
        error_messages={'required': 'Este campo es obligatorio'}
    )