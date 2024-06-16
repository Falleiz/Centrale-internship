from django.urls import path
from . import views

urlpatterns =[
   #PARTIE ETUDIANT
   path('',views.acceuil,name='acceuil'),
   path('login_page/',views.do_login_user,name='login'),
   path('login/',views.login_user),
   path('login_page/home/',views.home,name='home')   ,
   path('aide/',views.aide_page,name='aide'),
   path('alunis/',views.alumnis_page,name='alumnis'),
   path('login/',views.log_out,name='log_out'),
   path('secteur/',views.secteur_page,name='secteur'),
   path('secteur/<int:object_id>/',views.secteur_description,name='secteur_description'),
   path('offres/',views.offer_page,name='offres'),
   path('entreprise/',views.entreprise_page,name='entreprise'),
   path('entreprise/<int:object_id>/',views.entreprise_description,name='entreprise_description'),
   path('entretien/',views.entretien_page,name='entretien'),
   path('infos/<int:object_id>/',views.offer_description,name='infos'),
   path('infos_alunis/<int:object_id>/',views.alunis_infos_page,name='alunis_infos'),
   path('postuler/<int:object_id>',views.candidature_page,name='candidature'),
   
   #---------------------------------------------------------------------------------------------------------------#
   #PARTIE SERVICE DE SCOLARITE
   
   path('s_login/',views.s_login,name='s_login'),
   path('s_login/s_home/',views.service_home,name='service_home'),
   path('s_offre_list/',views.s_offre_list,name='s_offre_liste'),
   path('offres/<int:id>/modifier/', views.s_offre_modifier, name='s_offre_modifier'),  
   path('offres/<int:id>/supprimer/', views.s_offre_supprimer, name='s_offre_supprimer'),
   path('s_ajouter_offre/',views.s_ajouter_offre,name='s_ajouter_offre'),
   path('liste/',views.s_enterprise_liste,name='s_entrprise_liste'),
   path('entreprises/modifier/<int:pk>/', views.entreprise_modifier, name='entreprise_modifier'),
   path('entreprises/supprimer/<int:pk>/', views.entreprise_supprimer, name='entreprise_supprimer'),
   path('s_ajouter_entreprise/',views.s_ajouter_entreprise,name='s_ajouter_entreprise'),
   path('s_list_secteur/',views.s_liste_secteur,name='s_liste_secteur'),
   path('secteurs/ajouter/', views.ajouter_secteur, name='ajouter_secteur'),
   path('secteurs/supprimer/<int:pk>/', views.supprimer_secteur, name='supprimer_secteur'), 
     path('etudiants/',views.liste_etudiants, name='liste_etudiants'),
   path('secteurs/modifier/<int:pk>/', views.modifier_secteur, name='modifier_secteur'),
   path('etudiants/ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('etudiants/modifier/<int:pk>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('etudiants/supprimer/<int:pk>/', views.supprimer_etudiant, name='supprimer_etudiant'),
  path('alumnis/', views.liste_alumnis, name='liste_alumnis'),
    path('alumnis/ajouter/', views.ajouter_alumnis, name='ajouter_alumnis'),
    path('alumnis/modifier/<int:pk>/',views.modifier_alumnis, name='modifier_alumnis'),
    path('alumnis/supprimer/<int:pk>/', views.supprimer_alumnis, name='supprimer_alumnis'),

    
]
