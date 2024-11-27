from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm
from django.contrib import messages
from shop import settings
from django.core.mail import send_mail 
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

User = get_user_model()

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # Traiter le formulaire
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Vérifier si l'email est valide
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "L'adresse email n'est pas valide.")
            return redirect('signup')# Vérifier si l'email est valide
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "L'adresse email n'est pas valide.")
            return redirect('signup')

        # Vérifier si un utilisateur avec cet email existe déjà
        if User.objects.filter(email=email).exists():
            messages.error(request, "Un compte avec cet email existe déjà.")
            return redirect('signup')
        
        if not email:
            messages.error(request, "L'email est requis pour créer un compte.")
            return redirect('signup')

        # Création de l'utilisateur avec un email et un mot de passe
        user = User.objects.create_user(email=email, password=password)
        login(request, user)
        
        # Envoi d'un e-mail de bienvenue
        subject = "Bienvenue sur Sellerie la Vie en Rose"
        message = f"Bonjour,\n\nMerci de vous être inscrit sur notre site ! Nous sommes ravis de vous accueillir parmi nous."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
        return redirect('index')

    return render(request, 'accounts/signup.html')


def login_user(request):  #connecter l'utilisateur
    if request.method == 'POST':
       
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            full_message = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"
            try:
                send_mail(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,
                    ['enzo.tenis74@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, "Votre message a été envoyé avec succès.")
            except:
                messages.error(request, "Une erreur s'est produite lors de l'envoi de votre message. Veuillez réessayer plus tard.")
            return redirect('contact')
        else:
            messages.error(request, "Tous les champs sont requis.")

    return render(request, 'accounts/contact.html')