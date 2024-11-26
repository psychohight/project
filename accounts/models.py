from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from iso3166 import countries

# Create your models here.
class CustomUserManager(BaseUserManager): # Créer un gestionnaire d'utilisateurs
    def create_user(self, email, password, **kwargs): 
        if not email:
            raise ValueError('email obligatoire')
        
        
        email = self.normalize_email(email)       # normaliser l'email
        user = self.model(email=email, **kwargs)  # Créer un utilisateur
        user.set_password(password)               # Définir le mot de passe
        user.save()
        return user
    
    
    def create_superuser(self, email, password, **kwargs):
        kwargs['is_staff'] = True           # Superuser a accès à l'admin
        kwargs['is_superuser'] = True       # Superuser a tous les droits
        kwargs['is_active'] = True          
        
        return self.create_user(email=email, password=password, **kwargs)



class Shopper(AbstractUser): # Créer un modèle utilisateur
    username = None
    email = models.EmailField(unique=True)
    stripe_id = models.CharField(max_length=90, blank=True) # Champ pour l'identifiant de l'utilisateur sur Stripe
    
    USERNAME_FIELD = 'email' # champ unique
    REQUIRED_FIELDS = [] # champ obligatoire
    objects = CustomUserManager()
    

class ShippingAddress(models.Model): # Créer un modèle d'adresse de livraison
    user = models.ForeignKey(Shopper, on_delete=models.CASCADE) # Un utilisateur peut avoir plusieurs adresses
    name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=1024, help_text='adresse et numero')
    address_2 = models.CharField(max_length=1024, help_text='batiment, etages,...', blank=True)
    city = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=2, choices=[(c.alpha2.lower(), c.name) for c in countries]) # Champ pour le pays


