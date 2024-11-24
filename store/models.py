from django.utils import timezone
from django.db import models
from django.urls import reverse
from shop.settings import AUTH_USER_MODEL
# Créer un modèle
"""
Product
- Nom
- Prix
- Quantité
- Description
- Image
"""

class Product(models.Model):
    name = models.CharField(max_length=128) 
    slug = models.SlugField(max_length=128) # SlugField (champ pour les URL)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True) # blank=True (l'admin n'est pas obligé de remplir ce champ)
    image = models.ImageField(upload_to='products/', blank=True, null=True) # null=True (l'admin n'est pas obligé de remplir ce champ)

    def __str__(self):
        return self.name # Affiche le nom du produit dans l'admin

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug}) # Redirige vers la page du produit
    
# article
"""
-utilisateur
-produit
-quantité
-commande ou non
"""

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE) # Un utilisateur peut avoir plusieurs commandes
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})" # Affiche la quantité et le nom du produit dans l'admin




# panier
"""
-utilisateur
-articles
-commande ou non
-date de la commande
"""

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE) # Un utilisateur a un seul panier
    orders = models.ManyToManyField(Order)
    
    def __str__(self):
        return self.user.username # Affiche le nom d'utilisateur dans l'admin
    
    def delete(self, *args, **kwargs):      # Supprime les commandes du panier
        for order in self.orders.all():
            order.ordered = True
            order.order_date = timezone.now()
            order.save()
            
        self.orders.clear()                 # Supprime les commandes du panier
        super().delete(*args, **kwargs)