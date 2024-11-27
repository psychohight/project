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