document.addEventListener('DOMContentLoaded', function() {
    let timer;
    
    window.addEventListener('scroll', function() {
        // Ajoute la classe "flou" au body quand on fait défiler
        document.body.classList.add('flou');
        
        // Supprime la classe "flou" après un certain temps sans défilement
        clearTimeout(timer);
        timer = setTimeout(function() {
            document.body.classList.remove('flou');
        }, 200); // Le délai de 200 ms peut être ajusté selon vos préférences
    });
});
