import express from 'express';

export const products = [
  { id: 1, nom: 'Produit 1', prix: 20.00, image: 'images/ceinture1-0.jpg' },
  { id: 2, nom: 'Produit 2', prix: 20.00, image: 'images/ceinture2.jpg' }
    // Ajoutez ici les autres produits
];

const productsRoutes = express.Router();
  
  // Route pour obtenir la liste des produits
  productsRoutes.get('/', (req, res) => {
    res.json(products);
  });
  
  export default productsRoutes;
  