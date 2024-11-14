from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),  # Route pour la page d'accueil
    path('boutique/', views.index, name='boutique'),  # Route pour la page de boutique (par exemple)
    path('enregistrement/', views.enregistrement, name='enregistrement'), # Route pour la page d'enregistrement
    path('panier/', views.panier, name='panier'), # Route pour la page du panier
    
    
]
