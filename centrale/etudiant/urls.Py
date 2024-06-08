from django.urls import path
from . import views

urlpatterns =[
   path('',views.do_login_user,name='login'),
   path('login/',views.login_user),
   path('home/',views.home,name='home')   ,
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
  
]
