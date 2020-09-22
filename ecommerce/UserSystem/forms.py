from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_Registrations(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }