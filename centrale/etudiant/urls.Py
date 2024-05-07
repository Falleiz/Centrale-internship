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
   path('offres/',views.offer_page,name='offres'),
   path('entreprise/',views.entreprise_page,name='entreprise'),
   path('entretien/',views.entretien_page,name='entretien'),
   path('infos/',views.offer_description,name='infos'),
   path('infos_alunis/',views.alunis_infos_page,name='alunis_infos'),

     
]
