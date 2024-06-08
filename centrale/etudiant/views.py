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
