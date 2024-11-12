from django.db import models

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
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True) # blank=True (l'admin n'est pas obligé de remplir ce champ)
    image = models.ImageField(upload_to='products/', blank=True, null=True) # null=True (l'admin n'est pas obligé de remplir ce champ)

    def __str__(self):
        return self.name # Affiche le nom du produit dans l'admin
