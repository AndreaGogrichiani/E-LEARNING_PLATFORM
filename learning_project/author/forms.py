from django import forms
from .models import CustomUser, Courses
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["role", 'username', 'password1', 'password2']

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

class CourseForm(forms.Form):
    class Meta:
        model = Courses
        fields = ['name', 'description']