// Importation des modules
import express from 'express';
import cors from 'cors';
import productsRoutes from './routes/products.js';
import cartRoutes from './routes/cart.js';

const app = express();
const PORT = 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use('/api/products', productsRoutes);
app.use('/api/cart', cartRoutes);

// Démarrer le serveur
app.listen(PORT, () => {
  console.log(`Serveur écoute sur le port ${PORT}`);
});
