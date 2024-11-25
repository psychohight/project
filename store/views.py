from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
import stripe

from shop import settings
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

def create_checkout_session(request): # Vue pour créer une session de paiement
    stripe.api_key = settings.STRIPE_API_KEY
    cart = request.user.cart
    
    line_items = [{'price': order.product.stripe_id, 
                   'quantity': order.quantity} for order in cart.orders.all()]
    
    session = stripe.checkout.Session.create(
        locale='fr',
        payment_method_types=['card'],
        line_items= line_items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('checkout-success')),
        cancel_url='http://127.0.0.1:8000',
    )
    
    return redirect(session.url, code=303)

def checkout_success(request): # Vue pour afficher la page de paiement réussi
    return render(request, 'store/success.html')

def delete_cart(request): # Vue pour supprimer le panier
    cart = request.user.cart
    if cart:
        cart.orders.all().delete() 
        cart.delete()
        
    return redirect('index')