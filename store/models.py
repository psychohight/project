from django.db import models
from django.urls import reverse
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