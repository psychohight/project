// Mise à jour du compteur du panier
document.addEventListener('DOMContentLoaded', function() {
    var cartCount = document.getElementById('cart-count');

    function updateCartCount() {
        var cartItems = JSON.parse(localStorage.getItem('cart')) || [];
        cartCount.textContent = cartItems.length;
    }

    updateCartCount();
});

// Ajouter des produits au panier
document.addEventListener('DOMContentLoaded', function() {
    var boutonsAjouter = document.querySelectorAll('.btn-ajouter-panier');
    var cartCount = document.getElementById('cart-count');

    // Fonction pour mettre à jour le compteur du panier
    function updateCartCount() {
        var cartItems = JSON.parse(localStorage.getItem('cart')) || [];
        cartCount.textContent = cartItems.length;
    }

    // Mettre à jour le compteur au chargement de la page
    updateCartCount();

    boutonsAjouter.forEach(function(button) {
        button.addEventListener('click', function() {
            var produit = this.parentElement;
            var nom = produit.getAttribute('data-nom');
            var prix = parseFloat(produit.getAttribute('data-prix')); // Conversion en nombre
            var image = produit.getAttribute('data-image');

            var produitObj = {
                nom: nom,
                prix: prix,
                image: image,
                quantite: 1
            };

            // Récupérer le panier actuel
            var cartItems = JSON.parse(localStorage.getItem('cart')) || [];

            // Vérifier si le produit est déjà dans le panier
            var index = cartItems.findIndex(function(item) {
                return item.nom === nom;
            });

            if (index !== -1) {
                // Si le produit est déjà dans le panier, augmenter la quantité
                cartItems[index].quantite += 1;
            } else {
                // Sinon, ajouter le produit au panier
                cartItems.push(produitObj);
            }

            // Enregistrer le panier mis à jour dans le localStorage
            localStorage.setItem('cart', JSON.stringify(cartItems));

            // Mettre à jour le compteur du panier
            updateCartCount();

            alert(nom + " a été ajouté au panier.");
        });
    });
});

// Effet de flou lors du défilement
document.addEventListener('DOMContentLoaded', function() {
    var produits = document.querySelectorAll('.produit');

    var observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.01 // L'élément est visible à 1%
    });

    produits.forEach(function(produit) {
        observer.observe(produit);
    });
});
