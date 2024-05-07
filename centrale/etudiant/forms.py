from django import forms
from .models import Utilisateur

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())  # Hide password input

    class Meta:
        model = Utilisateur
        fields = ['first_name', 'last_name', 'email', 'password']
