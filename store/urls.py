from django.urls import path
from store.views import index
from store import views
from django.conf.urls.static import static

app_name = 'store'

urlpatterns = [
    path('', index, name='index'),  # Route pour la page d'accueil
    
]