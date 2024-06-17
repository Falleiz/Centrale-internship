from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Secteur(models.Model):
    nom = models.CharField(max_length=50)
    description=models.TextField()
    def __str__(self):
        return self.nom
       
class Users(User):
    secteur=models.ForeignKey(Secteur,null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.last_name +' '+self.first_name


class Entreprise(models.Model):
    nom=models.CharField(max_length=255,null=False,blank=False)
    secteur=models.CharField(max_length=255,default='*')
    description=models.TextField()
    ville=models.CharField(max_length=30)
    lien_map_ville=models.URLField()
    logo_url=models.URLField()
    lien_page_web=models.URLField(null=True)
    def __str__(self):
        return self.nom
    
    


class Offre_de_stage(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(null=True)
    Missions=models.TextField(null=True,blank=True)
    Profil_recherché=models.TextField(null=True,blank=True)
    Ce_que_nous_offrons=models.TextField(null=True,blank=True)
    secteur=models.CharField(max_length=200,default='*')
    class Type(models.TextChoices):
        observation='OBS','Observation'
        assistant_ingenieur= 'ASS_ENG','Assistant Ingenieur'
        final_project='PFE','Projet de fin d\'étude'
        Research='RES','Recherche'
    type_stage=models.CharField(max_length=10,choices=Type.choices)
    entrprise=models.CharField(max_length=200,default='*')
    ville=models.CharField(max_length=30)
    RH_email=models.EmailField()
    date_de_publication=models.DateField(auto_now_add=True)
    logo_url=models.URLField(blank=False,null=False)
    durée=models.IntegerField(default=2)
    def __str__(self):
        return self.titre
    

class Stage(models.Model):
    class Type(models.TextChoices):
        observation='OBS','Observation'
        assistant_ingenieur= 'ASS_ENG','Assistant Ingenieur'
        final_project='PFE','Projet de fin d\'étude'
        Research='RES','Recherche'        
    type=models.CharField(max_length=10,choices=Type.choices)
    secteur=models.ForeignKey(Secteur,null=True, blank=True, on_delete=models.SET_NULL)
    entreprise=models.ForeignKey(Entreprise,on_delete=models.CASCADE)
    def __str__(self):
        return self.entreprise.nom
    
class Alumnis(models.Model):
    nom=models.CharField(max_length=25,null=False,blank=False) 
    prenom=models.CharField(max_length=25,null=False,blank=False)
    promotion=models.IntegerField()
    email=models.EmailField(unique=True,null=False,blank=False)
    linkdn=models.URLField()
    photo=models.ImageField(null=True, blank=True)
    numero=PhoneNumberField()
    #section stage
    stage_1A_ville=models.CharField(max_length=30,default='*')
    stage_1A_secteur=models.CharField(max_length=30,default='*')
    stage_1A_entreprise=models.CharField(max_length=30,default='*')
    stage_2A_ville=models.CharField(max_length=30,default='*')
    stage_2A_secteur=models.CharField(max_length=30,default='*')
    stage_2A_entreprise=models.CharField(max_length=30,default='*')
    stage_3A_ville=models.CharField(max_length=30,default='*')
    stage_3A_secteur=models.CharField(max_length=30,default='*')
    stage_3A_entreprise=models.CharField(max_length=30,default='*')
    emploi_secteur=models.CharField(max_length=30,default='*')
    emploi_entreprise=models.CharField(max_length=30,default='*')
    def __str__(self):
        return self.nom +' '+self.prenom
    


class Candidature(models.Model):
    Offre = models.ForeignKey('Offre_de_stage', on_delete=models.CASCADE)
    etudiant = models.ForeignKey('Users', on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cvs/',default=None)
    lettre = models.FileField(upload_to='lettres/',default=None)

    def __str__(self):
        return f"{self.etudiant.first_name} {self.etudiant.last_name}"
    
    
#-------------------------------------------------------------------------------------------------------------------#
#PARTIE SERVICE STAGE   
from django.db.models import Q


class Service_users(User):
     def __str__(self):
        return self.last_name +' '+self.first_name
