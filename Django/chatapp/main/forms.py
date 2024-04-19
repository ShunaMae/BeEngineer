from django import forms 
from .models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Talk


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", )

class LoginForm(AuthenticationForm):
    pass

class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ("message", )

class UsernameChange(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", )
        labels = {"username": "New Username"}
        help_texts = {"username": ""}
    

class EmailChange(forms.ModelForm):
    class Meta:
        model=User
        fields = ('email', )
        