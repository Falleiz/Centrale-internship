from django import forms
from .models import Candidature

class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['cv', 'lettre']
        widgets = {
            'cv': forms.FileInput(attrs={'class': 'form-control'}),
            'lettre': forms.FileInput(attrs={'class': 'form-control'}),
        }
