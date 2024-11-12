// Script JavaScript pour la gestion du panier

document.addEventListener('DOMContentLoaded', function() {
    var cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    var cartItemsContainer = document.getElementById('cart-items');
    var totalPriceElement = document.getElementById('total-price');
    var cartCount = document.getElementById('cart-count');
    var clearCartButton = document.getElementById('clear-cart');

    // Fonction pour mettre à jour le compteur du panier
    function updateCartCount() {
        cartCount.textContent = cartItems.length;
    }

    // Fonction pour afficher les produits du panier
    function displayCartItems() {
        cartItemsContainer.innerHTML = '';
        var totalPrice = 0;

        cartItems.forEach(function(item, index) {
            var prix = parseFloat(item.prix); // Assurer que le prix est un nombre
            var quantite = parseInt(item.quantite); // Assurer que la quantité est un entier

            var subtotal = prix * quantite;
            totalPrice += subtotal;

            var tr = document.createElement('tr');

            tr.innerHTML = `
                <td><img src="${item.image}" alt="${item.nom}" width="50"></td>
                <td>${item.nom}</td>
                <td>€${prix.toFixed(2)}</td>
                <td>${quantite}</td>
                <td>€${subtotal.toFixed(2)}</td>
                <td><button class="btn-supprimer" data-index="${index}">Supprimer</button></td>
            `;

            cartItemsContainer.appendChild(tr);
        });

        totalPriceElement.textContent = totalPrice.toFixed(2);
        updateCartCount();
    }

    // Fonction pour supprimer un produit du panier
    cartItemsContainer.addEventListener('click', function(event) {
        if (event.target.classList.contains('btn-supprimer')) {
            var index = event.target.getAttribute('data-index');
            cartItems.splice(index, 1);
            localStorage.setItem('cart', JSON.stringify(cartItems));
            displayCartItems();
        }
    });

    // Fonction pour vider le panier
    clearCartButton.addEventListener('click', function() {
        cartItems = [];
        localStorage.removeItem('cart');
        displayCartItems();
    });

    // Afficher les produits au chargement de la page
    displayCartItems();
});

// Mise à jour du compteur du panier
document.addEventListener('DOMContentLoaded', function() {
    var cartCount = document.getElementById('cart-count');

    function updateCartCount() {
        var cartItems = JSON.parse(localStorage.getItem('cart')) || [];
        cartCount.textContent = cartItems.length;
    }

    updateCartCount();
});
