document.addEventListener("DOMContentLoaded", function () {
  // Obtient l'identifiant de la page depuis l'élément body
  const pageId = document.body.id;

  // Sélectionne le lien correspondant à l'identifiant de la page
  const activeLink = document.querySelector(
    `nav ul li a[data-page="${pageId}"]`
  );

  console.log("helllo");

  // Vérifie si un lien correspondant a été trouvé
  if (activeLink) {
    // Ajoute la classe 'active'
    activeLink.classList.add("active");
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var lastScrollTop = 0; // Stocke la dernière position de défilement
  var menuContainer = document.getElementById("menu-container");

  // Assurez-vous que le menu est visible quand on est au top de la page
  if (window.pageYOffset || document.documentElement.scrollTop === 0) {
    menuContainer.style.top = "0";
  }

  window.addEventListener(
    "scroll",
    function () {
      var currentScroll =
        window.pageYOffset || document.documentElement.scrollTop;

      // Affiche le menu si on est tout en haut de la page
      if (currentScroll <= 0) {
        menuContainer.style.top = "0";
      } else if (currentScroll > lastScrollTop) {
        // Cache le menu si on fait défiler vers le bas
        menuContainer.style.top = "-100%"; // Adaptez cette valeur à la hauteur de votre menu
      } else {
        // Affiche le menu si on fait défiler vers le haut
        menuContainer.style.top = "0";
      }
      lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // Mise à jour de la dernière position de défilement
    },
    false
  );
});
