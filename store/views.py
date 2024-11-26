
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
import stripe
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Shopper
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
        payment_method_types=['card'],
        line_items= line_items,
        mode='payment',
        locale='fr',
        customer_email=request.user.email,
        shipping_address_collection={'allowed_countries': ['FR', 'US']},
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

@csrf_exempt
def stripe_webhook(request): # Vue pour gérer les webhooks de Stripe
    playload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = 'whsec_fa329b2814ba0e98fb0625445ebeb82d394e812870fe8ce627520bdec147608c' # Clé secrète de l'endpoint
    event = None
    
    try:
        event = stripe.Webhook.construct_event(
            playload, sig_header, endpoint_secret 
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        data = event['data']['object']
        try:
            user = get_object_or_404(Shopper, email=data['customer_details']['email'])
        except KeyError:
            return HttpResponse('invalid user email', status=400)
        
        complete_order(data=data, user=user)
        save_shipping_address(data=data, user=user)
        return HttpResponse(status=200)
    
    return HttpResponse(status=200)

def complete_order(data, user): # Vue pour compléter la commande
    user.strip_id = data['customer']
    user.cart.delete()
    user.save()
    return HttpResponse(status=200)

def save_shipping_address(data, user):
    pass