from django.shortcuts import render
from store.models import Product

# Create your views here.
def index(request):
    Products = Product.objects.all()
    
    return render(request, 'index.html', context={'products': Products})

def boutique(request):
    products = Product.objects.all()
    return render(request, 'boutique.html', context={'products': products})

def enregistrement(request):
    return render(request, 'enregistrement.html')

def panier(request):
    return render(request, 'panier.html')

