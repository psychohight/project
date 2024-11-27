document.addEventListener('DOMContentLoaded', function () {
    // Sélectionne tous les éléments à observer (sections, conteneur de titre, pied de page, navigation, etc.)
    var elements = document.querySelectorAll('section, .title-container, footer, nav');

    // Crée un observer pour surveiller les éléments quand ils entrent et sortent de la vue
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                // Lorsque l'élément entre dans la vue, ajoute la classe 'visible' pour appliquer l'effet
                entry.target.classList.add('visible');
            } else {
                // Lorsque l'élément sort de la vue, supprime la classe 'visible'
                entry.target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1 // L'élément est considéré visible à partir de 10% visible
    });

    // Observe chaque élément sélectionné
    elements.forEach(function (element) {
        observer.observe(element);
    });
});



