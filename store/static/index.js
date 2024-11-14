// Gestion du menu déroulant
document.addEventListener('DOMContentLoaded', function() {
    var dropbtn = document.querySelector('.dropbtn');
    var dropdownContent = document.querySelector('.dropdown-content');

    dropbtn.addEventListener('click', function(event) {
        event.preventDefault();
        dropdownContent.classList.toggle('show');
    });

    // Ferme le menu déroulant si l'utilisateur clique en dehors
    window.addEventListener('click', function(event) {
        if (!event.target.matches('.dropbtn')) {
            if (dropdownContent.classList.contains('show')) {
                dropdownContent.classList.remove('show');
            }
        }
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
        threshold: 0.1 // L'élément est visible à 10%
    });

    produits.forEach(function(produit) {
        observer.observe(produit);
    });
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

// Animation du fond d'étoiles
const canvas = document.getElementById('star-canvas');
const ctx = canvas.getContext('2d');
let stars = [];
const numStars = 150;

// Redimensionne le canvas pour s'adapter à la fenêtre
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// Initialiser les étoiles
function createStars() {
    stars = [];
    for (let i = 0; i < numStars; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 7,
            speedX: (Math.random() - 0.25) * 0.25,
            speedY: (Math.random() - 0.25) * 0.25
        });
    }
}

// Dessiner les étoiles sous forme de petites figures irrégulières
function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'white';
    stars.forEach(star => {
        ctx.beginPath();
        let spikes = 5 + Math.floor(Math.random() * 3); // Nombre de pointes (irrégularité des étoiles)
        let outerRadius = star.radius;
        let innerRadius = star.radius / 2;

        for (let i = 0; i < spikes * 2; i++) {
            let radius = (i % 2 === 0) ? outerRadius : innerRadius;
            let angle = (i * Math.PI) / spikes;
            ctx.lineTo(
                star.x + radius * Math.cos(angle),
                star.y + radius * Math.sin(angle)
            );
        }

        ctx.closePath();
        ctx.fill();
    });
}

// Mettre à jour la position des étoiles
function updateStars() {
    stars.forEach(star => {
        star.x += star.speedX;
        star.y += star.speedY;

        // Replacer les étoiles lorsqu'elles quittent l'écran
        if (star.x < 0) star.x = canvas.width;
        if (star.x > canvas.width) star.x = 0;
        if (star.y < 0) star.y = canvas.height;
        if (star.y > canvas.height) star.y = 0;
    });
}

// Animation
function animate() {
    updateStars();
    drawStars();
    requestAnimationFrame(animate);
}

// Initialiser et lancer l'animation
createStars();
animate();
