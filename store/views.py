from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from store.models import Cart, Order, Product 

# Create your views here.
def index(request): # Vue pour afficher la page d'accueil
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'products': products})

# ----------------DETAIL PRODUITS----------------

def product_detail(request, slug): # Vue pour afficher les détails d'un produit
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={'product': product})

# ----------------PANIER----------------


def add_to_cart(request, slug):
    user = request.user                             # Récupère l'utilisateur connecté
    product = get_object_or_404(Product, slug=slug) # Récupère le produit
    cart, _ = Cart.objects.get_or_create(user=user) # Crée un panier pour l'utilisateur s'il n'en a pas
    order, create = Order.objects.get_or_create(user=user,
                                                ordered=False,
                                                product=product) # Crée une commande pour l'utilisateur s'il n'en a pas
    if create:
        cart.orders.add(order) # Ajoute la commande au panier
        cart.save()
    else:
        order.quantity += 1    # Incrémente la quantité
        order.save()
    
    return redirect(reverse('product', kwargs={'slug': slug})) # Redirige vers la page du produit


def cart(request): # Vue pour afficher le panier
    cart = get_object_or_404(Cart, user=request.user)
    
    return render(request, 'store/cart.html', context={'orders': cart.orders.all()}) # Affiche les commandes du panier

def delete_cart(request): # Vue pour supprimer le panier
    cart = request.user.cart
    if cart:
        cart.orders.all().delete() 
        cart.delete()
        
    return redirect('index')