from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    username = forms.CharField(label='username')
    first_name = forms.CharField(label='first_name')
    password1 = forms.CharField(widget=forms.PasswordInput, label='password1')
    password2 = forms.CharField(widget=forms.PasswordInput, label='password2')

    class Meta:
        model = User
        fields = ("first_name", "username", "password1", "password2")