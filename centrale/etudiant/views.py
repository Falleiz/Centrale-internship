from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  # For protecting views
from .models import Users
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
    return render(request,'home.html',{'user':user})

def log_out(request):
     logout(request)
     return redirect('login')

def aide_page(request):
    return render(request, 'aide.html')

def alumnis_page(request):
    return render(request,'alunis-liste.html')

def secteur_page(request):
    return render(request,'secteur.html')

def offer_page(request):
    return render(request,'offres.html')

def entreprise_page(request):
    return render(request,'entreprise.html')

def entretien_page(request):
    return render(request,'entretien.html')

def offer_description(request):
    return render(request,'description_offres.html')

def alunis_infos_page(request):
    return render(request,'alunis_infos.html')