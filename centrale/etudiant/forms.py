from django import forms
from .models import Candidature,Offre_de_stage

class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['cv', 'lettre']
        widgets = {
            'cv': forms.FileInput(attrs={'class': 'form-control'}),
            'lettre': forms.FileInput(attrs={'class': 'form-control'}),
        }

class OffreDeStageForm(forms.ModelForm):
    class Meta:
        model = Offre_de_stage
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'offre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'Missions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Missions'}),
            'Profil_recherché': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Profil recherché'}),
            'Ce_que_nous_offrons': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ce que nous offrons'}),
            'secteur': forms.Select(attrs={'class': 'form-control'}),
            'type_stage': forms.Select(attrs={'class': 'form-control'}),
            'entrprise': forms.Select(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'RH_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email RH'}),
            'logo_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL du logo'}),
            'durée': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Durée en mois'}),
        }