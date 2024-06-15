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
]
