from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm
from django.contrib import messages

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        # Traiter le formulaire
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email:
            messages.error(request, "L'email est requis pour créer un compte.")
            return redirect('signup')

        # Création de l'utilisateur avec un email et un mot de passe
        user = User.objects.create_user(email=email, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')


def login_user(request):  #connecter l'utilisateur
    if request.method == 'POST':
       
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
            
    return render(request, 'accounts/login.html')



def logout_user(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    if request.method == 'POST':
        current_password = request.POST.get('password')
        if request.user.check_password(current_password):
            user = request.user
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            messages.success(request, 'Profil mis à jour avec succès.')
        else:
            messages.error(request, 'Mot de passe incorrect.')

        return redirect('profile')

    form = UserForm(initial=model_to_dict(request.user, exclude=['password']))
    return render(request, 'accounts/profile.html', context={'form': form})
