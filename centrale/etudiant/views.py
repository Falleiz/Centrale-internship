from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  # For protecting views
from .models import Users,Alumnis,Offre_de_stage,Entreprise,Secteur,Candidature
from .forms import CandidatureForm


def acceuil(request):
    return render(request,'Accueil.html')
def login_user(request):
    return render(request,'login_page.html')


def do_login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email',None)
        password=request.POST.get('password',None)
        if email !=None and password !=None:
            print(f'email_recuperer: {email}\n password: {password}')
            try:
                user=Users.objects.get(email=email,password=password)
                if user:
                    print(f'usrname:{user.get_username()}')
                    login(request,user)
                    return redirect('home/')
            except :

                return render(request, 'login_page.html', {'error': 'Invalid username or password'})

                     
           
    return render(request, 'login_page.html')

def home(request):
    user=request.user
    offre=Offre_de_stage.objects.all()
    return render(request,'home.html',{'user':user,'offre':offre})

def log_out(request):
     logout(request)
     return redirect('login')
 
@login_required
def aide_page(request):
    return render(request, 'aide.html')

from django.shortcuts import render
from .models import Alumnis, Stage

@login_required
def alumnis_page(request):
    search_query = request.GET.get('search', '')
    company_filter = request.GET.get('company', '')
    sector_filter = request.GET.get('sector', '')

    alumni_list = Alumnis.objects.all()

    if search_query:
        alumni_list = alumni_list.filter(nom__icontains=search_query) | alumni_list.filter(prenom__icontains=search_query)

    if company_filter:
        alumni_list = alumni_list.filter(stage_1A__entreprise__nom__icontains=company_filter) | \
                      alumni_list.filter(stage_2A__entreprise__nom__icontains=company_filter) | \
                      alumni_list.filter(stage_3A__entreprise__nom__icontains=company_filter)

    if sector_filter:
        alumni_list = alumni_list.filter(stage_1A__secteur__nom__icontains=sector_filter) | \
                      alumni_list.filter(stage_2A__secteur__nom__icontains=sector_filter) | \
                      alumni_list.filter(stage_3A__secteur__nom__icontains=sector_filter)

    companies = Stage.objects.values_list('entreprise__nom', flat=True).distinct()
    sectors = Stage.objects.values_list('secteur__nom', flat=True).distinct()

    return render(request, 'alunis-liste.html', {
        'all_object': alumni_list,
        'companies': companies,
        'sectors': sectors,
        'search_query': search_query,
        'company_filter': company_filter,
        'sector_filter': sector_filter,
    })
@login_required
def secteur_page(request):
    search_query = request.GET.get('search', '')
    print('je suis')
    if search_query:
        all_secteur = Secteur.objects.filter(nom__icontains=search_query)
    else:
        all_secteur = Secteur.objects.all()
    
    return render(request, 'secteur.html', {'all_secteur': all_secteur, 'search_query': search_query})


@login_required
def secteur_description(request,object_id):
    secteur=get_object_or_404(Secteur,id=object_id)
        #Partie recommendation de cours 
    df = pd.read_csv('media\modified_coursea_data.csv')

    # Accept user input for preferences
    user_preferences = secteur.nom

    # Combine course titles and categories into a single text
    course_data = df['course_title'] + " " + df['category']

    # Initialize TF-IDF vectorizer and transform course data into feature vectors
    tfidf_vectorizer = TfidfVectorizer()
    course_features = tfidf_vectorizer.fit_transform(course_data)

    # Train a Nearest Neighbors model using all the data
    model = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='cosine')
    model.fit(course_features)

    # Transform user preferences into a feature vector
    user_vector = tfidf_vectorizer.transform([user_preferences])

    # Find the nearest neighbors (similar courses) to the user preferences
    distances, indices = model.kneighbors(user_vector)

    # Get the titles of the recommended courses
    recommended_courses = df.iloc[indices[0]]['course_title']
   

    return render(request,'secteur_description.html',{'secteur': secteur,'recommended_courses':recommended_courses})
    
@login_required  
def offer_page(request):
    search_query = request.GET.get('search', '')
    location_filter = request.GET.get('lieu', '')
    sector_filter = request.GET.get('secteur', '')
    type_filter = request.GET.get('type', '')
    entreprise_filter = request.GET.get('entreprise', '')

    offres = Offre_de_stage.objects.all()

    if search_query:
        offres = offres.filter(titre__icontains=search_query)

    if location_filter:
        offres = offres.filter(ville__icontains=location_filter)

    if sector_filter:
        offres = offres.filter(secteur__nom__icontains=sector_filter)

    if type_filter:
        offres = offres.filter(type_stage__icontains=type_filter)

    if entreprise_filter:
        offres = offres.filter(entrprise__nom__icontains=entreprise_filter)

    entreprises = Entreprise.objects.all()

    return render(request, 'offres.html', {
        'offre': offres,
        'entreprises': entreprises,
        'type_filter':type_filter
    })

@login_required    
def entreprise_page(request):
    search_query = request.GET.get('search', '')
    sector_filter = request.GET.get('sector', '')
    location_filter = request.GET.get('location', '')

    all_entreprise = Entreprise.objects.all()

    if search_query:
        all_entreprise = all_entreprise.filter(nom__icontains=search_query)

    if sector_filter:
        all_entreprise = all_entreprise.filter(secteur__nom__icontains=sector_filter)

    if location_filter:
        all_entreprise = all_entreprise.filter(ville__icontains=location_filter)

    sectors = Secteur.objects.all()
    locations = Entreprise.objects.values_list('ville', flat=True).distinct()

    return render(request, 'entreprise.html', {
        'all_entreprise': all_entreprise,
        'sectors': sectors,
        'locations': locations,
        'search_query': search_query,
        'sector_filter': sector_filter,
        'location_filter': location_filter,
    })
   
   
@login_required
def entreprise_description(request,object_id):
    entreprise=get_object_or_404(Entreprise,id=object_id)
    return render(request,'entreprise_description.html',{'entreprise': entreprise})
    
@login_required   
def entretien_page(request):
    return render(request,'entretien.html')

@login_required
def offer_description(request,object_id):
    object = get_object_or_404(Offre_de_stage, id=object_id)
   
    return render(request,'description_offres.html',{'object': object})

@login_required
def alunis_infos_page(request,object_id):
    object = get_object_or_404(Alumnis, id=object_id)
    
    return render(request,'alunis_infos.html', {'object': object})


User = get_user_model()
@login_required
def candidature_page(request, object_id):
    user = request.user
    user_instance = Users.objects.get(pk=request.user.pk)
    offre = get_object_or_404(Offre_de_stage, id=object_id)
    
    if request.method == 'POST':
        form = CandidatureForm(request.POST, request.FILES)
        if form.is_valid():
            candidature = form.save(commit=False)
            candidature.etudiant = user_instance
            candidature.Offre = offre
            candidature.save()
            return redirect('offres')  # Redirigez vers une vue de succès appropriée
    else:
        form = CandidatureForm()
    
    return render(request, 'candidature.html', {'form': form, 'offre': offre})



#------------------------------------------------------------------------------------------------------------------#
#Partie S_login page

from .models import Service_users
from django.db.models import Q
from .forms import OffreDeStageForm,EntrepriseForm,SecteurForm, UserForm,AlumnisForm

def s_login(request):
        if request.method == 'POST':
            username = request.POST.get('name',None)
            password=request.POST.get('password',None)
            if username !=None and password !=None:
                print(f'email_recuperer: {username}\n password: {password}')
                try:
                    user=Service_users.objects.get(username=username,password=password)
                    if user:
                        print(f'usrname:{user.get_username()}')
                        login(request,user)
                        return redirect('s_home/')
                except :

                    return render(request, 's_login.html', {'error': 'Invalid username or password'})


        return render(request,'s_login.html')
    

def service_home(request):
    user=request.user
    return render(request, 'S_home.html',{'user':user})

def s_offre_list(request):
    query = request.GET.get('q', '')
    filtre_titre = request.GET.get('titre', '')
    filtre_entreprise = request.GET.get('entreprise', '')
    filtre_secteur = request.GET.get('secteur', '')
    filtre_duree = request.GET.get('duree', '')
    filtre_type_stage = request.GET.get('type_stage', '')

    offres = Offre_de_stage.objects.all()

    if filtre_titre:
        offres = offres.filter(titre__icontains=filtre_titre)
    if filtre_entreprise:
        offres = offres.filter(entrprise__nom__icontains=filtre_entreprise)
    if filtre_secteur:
        offres = offres.filter(secteur__nom__icontains=filtre_secteur)
    if filtre_duree:
        offres = offres.filter(durée__iexact=filtre_duree)
    if filtre_type_stage:
        offres = offres.filter(type_stage__iexact=filtre_type_stage)
    if query:
        offres = offres.filter(
            Q(titre__icontains=query) |
            Q(entrprise__nom__icontains=query) |
            Q(secteur__nom__icontains=query) |
            Q(durée__iexact=query) |
            Q(type_stage__iexact=query)
        )

    return render(request, 's_offre_liste.html', {'offres': offres})



def s_offre_modifier(request, id):
    offre = get_object_or_404(Offre_de_stage, id=id)
    if request.method == 'POST':
        form = OffreDeStageForm(request.POST, instance=offre)
        if form.is_valid():
            form.save()
            return redirect('s_offre_liste')
    else:
        form = OffreDeStageForm(instance=offre)
    return render(request, 's_modifier_offre.html', {'form': form, 'offre': offre})


def s_offre_supprimer(request, id):
    offre = get_object_or_404(Offre_de_stage, id=id)
    if request.method == 'POST':
        offre.delete()
        return redirect('s_offre_liste')
    return render(request, 'supprimer_offre.html', {'offre': offre})

def s_ajouter_offre(request):
    if request.method == 'POST':
        form = OffreDeStageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('s_offre_liste')  
    else:
        form = OffreDeStageForm()
    return render(request, 's_ajouter_offre.html', {'form': form})


def s_enterprise_liste(request):
    entreprises = Entreprise.objects.all()
    
    search_nom = request.GET.get('search_nom')
    search_ville = request.GET.get('search_ville')
    search_secteur = request.GET.get('search_secteur')

    if search_nom:
        entreprises = entreprises.filter(nom__icontains=search_nom)
    if search_ville:
        entreprises = entreprises.filter(ville__icontains=search_ville)
    if search_secteur:
        entreprises = entreprises.filter(secteur__nom__icontains=search_secteur)

    secteurs = Secteur.objects.all()
    
    return render(request, 's_entreprises_liste.html', {'entreprises': entreprises, 'secteurs': secteurs})


def entreprise_modifier(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk)
    if request.method == "POST":
        form = EntrepriseForm(request.POST, instance=entreprise)
        if form.is_valid():
            form.save()
            return redirect('s_entrprise_liste')
    else:
        form = EntrepriseForm(instance=entreprise)
    return render(request, 'entreprise_modifier.html', {'form': form})

def entreprise_supprimer(request, pk):
    entreprise = get_object_or_404(Entreprise, pk=pk)
    if request.method == "POST":
        entreprise.delete()
        return redirect('s_entrprise_liste')
    return render(request, 'entreprise_supprimer.html', {'entreprise': entreprise})

def s_ajouter_entreprise(request):
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('s_entrprise_liste')
    else:
        form = EntrepriseForm()
    return render(request, 's_ajouter_entreprise.html', {'form': form})


def s_liste_secteur(request):
    query = request.GET.get('search')
    if query:
        secteurs = Secteur.objects.filter(nom__icontains=query)
    else:
        secteurs = Secteur.objects.all()
    return render(request, 's_liste_secteur.html', {'secteurs': secteurs})


def ajouter_secteur(request):
    if request.method == 'POST':
        form = SecteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('s_liste_secteur')
    else:
        form = SecteurForm()
    return render(request, 'ajouter_secteur.html', {'form': form})

def supprimer_secteur(request, pk):
    secteur = get_object_or_404(Secteur, pk=pk)
    if request.method == 'POST':
        secteur.delete()
        return redirect('s_liste_secteur')
    return render(request, 'supprimer_secteur.html', {'secteur': secteur})

def modifier_secteur(request, pk):
    secteur = get_object_or_404(Secteur, pk=pk)
    if request.method == 'POST':
        form = SecteurForm(request.POST, instance=secteur)
        if form.is_valid():
            form.save()
            return redirect('s_liste_secteur')
    else:
        form = SecteurForm(instance=secteur)
    return render(request, 'modifier_secteur.html', {'form': form, 'secteur': secteur})





def liste_etudiants(request):
    query = request.GET.get('search')
    if query:
        etudiants = Users.objects.filter(last_name__icontains=query) | Users.objects.filter(first_name__icontains=query)
    else:
        etudiants = Users.objects.all()
    return render(request, 'liste_etudiants.html', {'etudiants': etudiants})


def ajouter_etudiant(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = UserForm()
    return render(request, 'ajouter_etudiant.html', {'form': form})

def modifier_etudiant(request, pk):
    etudiant = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = UserForm(instance=etudiant)
    return render(request, 'modifier_etudiant.html', {'form': form, 'etudiant': etudiant})

def supprimer_etudiant(request, pk):
    etudiant = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'supprimer_etudiant.html', {'etudiant': etudiant})



def liste_alumnis(request):
    query = request.GET.get('search')
    secteur = request.GET.get('secteur')
    entreprise = request.GET.get('entreprise')
    ville = request.GET.get('ville')

    alumnis = Alumnis.objects.all()
    if query:
        alumnis = alumnis.filter(nom__icontains=query) | alumnis.filter(prenom__icontains=query)
    if secteur:
        alumnis = alumnis.filter(stage_1A__secteur__icontains=secteur) | alumnis.filter(stage_2A__secteur__icontains=secteur) | alumnis.filter(stage_3A__secteur__icontains=secteur) | alumnis.filter(emploi__secteur__icontains=secteur)
    if entreprise:
        alumnis = alumnis.filter(stage_1A__entreprise__icontains=entreprise) | alumnis.filter(stage_2A__entreprise__icontains=entreprise) | alumnis.filter(stage_3A__entreprise__icontains=entreprise) | alumnis.filter(emploi__entreprise__icontains=entreprise)
    if ville:
        alumnis = alumnis.filter(stage_1A__ville__icontains=ville) | alumnis.filter(stage_2A__ville__icontains=ville) | alumnis.filter(stage_3A__ville__icontains=ville) | alumnis.filter(emploi__ville__icontains=ville)

    return render(request, 'liste_alumnis.html', {'alumnis': alumnis})

def ajouter_alumnis(request):
    if request.method == 'POST':
        form = AlumnisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_alumnis')
    else:
        form = AlumnisForm()
    return render(request, 'ajouter_alumnis.html', {'form': form})

def modifier_alumnis(request, pk):
    alumnis = get_object_or_404(Alumnis, pk=pk)
    if request.method == 'POST':
        form = AlumnisForm(request.POST, request.FILES, instance=alumnis)
        if form.is_valid():
            form.save()
            return redirect('liste_alumnis')
    else:
        form = AlumnisForm(instance=alumnis)
    return render(request, 'modifier_alumnis.html', {'form': form, 'alumnis': alumnis})

def supprimer_alumnis(request, pk):
    alumnis = get_object_or_404(Alumnis, pk=pk)
    if request.method == 'POST':
        alumnis.delete()
        return redirect('liste_alumnis')
    return render(request, 'supprimer_alumnis.html', {'alumnis': alumnis})