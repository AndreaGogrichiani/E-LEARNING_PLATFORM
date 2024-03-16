from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def password_confirmation(self):
        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2


class LoginForm(forms.Form):
    model = User
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)