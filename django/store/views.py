from django.shortcuts import render
from store.models import Product

# Create your views here.
def index(request):
    Products = Product.objects.all()
    
    return render(request, 'index.html', context={'products': Products})