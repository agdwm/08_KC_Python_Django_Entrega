from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


from blogs.models import Post, Blog


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


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["blog"]

        #release_date = forms.DateTimeField(widget=forms.SplitDateTimeWidget())


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "blogtitle"]

    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label="First Name",
        error_messages={'required': 'This field is required'}
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label="Last Name",
        error_messages={'required': 'This field is required'}
    )
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Username",
        error_messages={'required': 'This field is required'}
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label="Email",
        error_messages = {'required': 'This field is required'}
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password",
        error_messages={'required': 'This field is required'},
        strip=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password confirmation",
        error_messages={'required': 'This field is required'},
        strip=False,
        help_text=("Enter the same password as before, for verification.")
    )
    blogtitle = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Blog Name",
        error_messages={'required': 'This field is required'}
    )
