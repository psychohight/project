import express from 'express';
import { products } from './products.js';

let cart = [];

const cartRoutes = express.Router();

cartRoutes.post('/', (req, res) => {
  const { productId, quantite } = req.body;
  const product = products.find(p => p.id === productId);
  if (product) {
    cart.push({ ...product, quantite });
    res.json({ message: 'Produit ajouté au panier', cart });
  } else {
    res.status(404).json({ message: 'Produit non trouvé' });
  }
});

cartRoutes.delete('/', (req, res) => {
  cart = [];
  res.json({ message: 'Panier vidé' });
});

export default cartRoutes;
