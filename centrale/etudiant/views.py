from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  # For protecting views
from .models import Users,Alumnis,Offre_de_stage,Entreprise
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

def aide_page(request):
    return render(request, 'aide.html')

from django.shortcuts import render
from .models import Alumnis, Stage

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

def secteur_page(request):
    return render(request,'secteur.html')

def offer_page(request):
    offre=Offre_de_stage.objects.all()
    return render(request,'offres.html',{'offre':offre})

def entreprise_page(request,):
    all_entreprise= Entreprise.objects.all()
   
    return render(request,'entreprise.html',{'all_entreprise': all_entreprise})

def entreprise_description(request,object_id):
    entreprise=get_object_or_404(Entreprise,id=object_id)
    return render(request,'entreprise_description.html',{'entreprise': entreprise})
    
    
def entretien_page(request):
    return render(request,'entretien.html')

def offer_description(request,object_id):
    object = get_object_or_404(Offre_de_stage, id=object_id)
   
    return render(request,'description_offres.html',{'object': object})

def alunis_infos_page(request,object_id):
    object = get_object_or_404(Alumnis, id=object_id)
    
    return render(request,'alunis_infos.html', {'object': object})