from django.contrib import admin
from.models import Users,Secteur,Entreprise,Offre_de_stage,Stage,Alumnis,Candidature
# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','password','username']

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display=['id','nom','secteur','description','logo_url','ville','lien_map_ville','lien_page_web']

@admin.register(Secteur)
class SecteurAdmin(admin.ModelAdmin):
    list_display=['id','nom','description']


@admin.register(Offre_de_stage)
class Offre_de_stageAdmin(admin.ModelAdmin):
    list_display = ['id','titre','secteur','description','type_stage','entrprise','durée','ville','RH_email','date_de_publication','logo_url']
    list_editable = ('titre','secteur','description','type_stage','entrprise','durée','ville','RH_email','logo_url')

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display=['id','type','secteur','entreprise']

@admin.register(Alumnis)
class AlumnisAdmin(admin.ModelAdmin):
    list_display=['id','nom','prenom','email','numero','stage_1A','stage_2A','stage_3A','emploi','photo']

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    pass