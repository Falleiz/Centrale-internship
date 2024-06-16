from django import forms
from .models import Candidature,Offre_de_stage,Entreprise,Secteur,Users,Alumnis,Stage

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
        
        
class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['nom', 'secteur', 'description', 'ville', 'lien_map_ville', 'logo_url', 'lien_page_web']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'entreprise'}),
            'secteur': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description de l\'entreprise'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'lien_map_ville': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Lien Google Maps'}),
            'logo_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL du logo'}),
            'lien_page_web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Lien de la page web'}),
        }
        

class SecteurForm(forms.ModelForm):
    class Meta:
        model = Secteur
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du secteur'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description du secteur'}),
        }
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'email', 'secteur','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse e-mail'}),
            'secteur': forms.Select(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
            
        }


class AlumnisForm(forms.ModelForm):
    class Meta:
        model = Alumnis
        fields = ['nom', 'prenom', 'promotion', 'email', 'linkdn', 'photo', 'numero', 'stage_1A', 'stage_2A', 'stage_3A', 'emploi']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'promotion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promotion'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'linkdn': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
            'stage_1A': forms.Select(attrs={'class': 'form-control'}),
            'stage_2A': forms.Select(attrs={'class': 'form-control'}),
            'stage_3A': forms.Select(attrs={'class': 'form-control'}),
            'emploi': forms.Select(attrs={'class': 'form-control'}),
        }
        
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['type', 'secteur', 'entreprise']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'secteur': forms.Select(attrs={'class': 'form-control'}),
            'entreprise': forms.Select(attrs={'class': 'form-control'}),
        }