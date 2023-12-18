const products = document.querySelectorAll(".product");

products.forEach((product) => {
  const wrapper = product.querySelector(".single-product-wrapper");
  const wrapperHover = product.querySelector(".single-product-wrapper-hover");

  product.addEventListener("mouseenter", () => {
    wrapperHover.classList.remove("d-none");
    wrapper.classList.add("d-none");
  });

  product.addEventListener("mouseleave", () => {
    wrapperHover.classList.add("d-none");
    wrapper.classList.remove("d-none");
  });
});

// Nav et link top
// Seuil de défilement pour la barre de navigation
const seuilDeDefilementNav = 220;

// Seuil de défilement pour le lien circulaire
const seuilDeDefilementlinkTop = 300;

// Nav
const nav = document.querySelector(".navbar");
const linkTop = document.querySelector(".go-top-link");

window.addEventListener("scroll", () => {
  const positionDeDefilement = window.scrollY;

  // Animation de la barre de navigation
  if (
    positionDeDefilement >= seuilDeDefilementNav &&
    !nav.classList.contains("sticky-top")
  ) {
    nav.classList.add("shadow-bottom");
    nav.style.animation = "slideIn 0.3s ease-in-out";
    nav.classList.add("sticky-top");
  } else if (
    positionDeDefilement < seuilDeDefilementNav &&
    nav.classList.contains("sticky-top")
  ) {
    nav.classList.remove("shadow-bottom");
    nav.style.animation = "slideOut 0.3s ease-in-out";
    setTimeout(() => {
      nav.classList.remove("sticky-top");
      nav.style.animation = "";
    }, 300);
  }

  // Animation du lien top
  if (positionDeDefilement >= seuilDeDefilementlinkTop) {
    linkTop.classList.remove("d-none");
  } else {
    linkTop.style.animation = "slide-out 0.3s forwards";
    setTimeout(() => {
      linkTop.classList.add("d-none");
      linkTop.style.animation = "";
    }, 300);
  }
});

// Aside

document.addEventListener("DOMContentLoaded", function () {
  const accordionButtons = document.querySelectorAll(".accordion-button");

  // Ajoutez un gestionnaire d'événements pour chaque bouton du menu d'accordéon
  accordionButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Fermez toutes les sections du menu d'accordéon
      accordionButtons.forEach((otherButton) => {
        if (otherButton !== button) {
          const target = document.querySelector(
            otherButton.getAttribute("data-bs-target")
          );
          if (target.classList.contains("show")) {
            const bsCollapse = new bootstrap.Collapse(target);
            bsCollapse.hide();
          }
        }
      });
    });
  });
});

// Fonction pour activer la navigation par onglets
function activateTab(tabId) {
  // Désactive tous les onglets et les contenus
  const tabs = document.querySelectorAll(".nav-link");
  tabs.forEach((tab) => {
    tab.classList.remove("active");
  });

  const tabContents = document.querySelectorAll(".tab-pane");
  tabContents.forEach((content) => {
    content.classList.remove("show", "active");
  });

  // Active l'onglet et le contenu correspondants
  const activeTab = document.querySelector(`#${tabId}`);
  if (activeTab) {
    activeTab.classList.add("show", "active");
    const correspondingNavLink = document.querySelector(`[href="#${tabId}"]`);
    if (correspondingNavLink) {
      correspondingNavLink.classList.add("active");
    }
  }
}

// Ajoutez un écouteur d'événement pour chaque lien d'onglet
const tabLinks = document.querySelectorAll(".pill-nav-link");
tabLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    event.preventDefault(); // Empêche le comportement par défaut du lien
    const tabId = link.getAttribute("href").substring(1); // Récupère l'identifiant de l'onglet
    activateTab(tabId); // Active l'onglet correspondant
  });
});

// Active le premier onglet au chargement de la page
activateTab("ex1-pills-1");

// Fonction pour changer l'image principale
function changeMainImage(imageUrl) {
  const mainImage = document.querySelector("#main-image");
  mainImage.src = imageUrl;
}

// Sélectionnez toutes les miniatures
const thumbnails = document.querySelectorAll(".item-thumb");

// Ajoutez un écouteur d'événements à chaque miniature
thumbnails.forEach((thumbnail) => {
  thumbnail.addEventListener("click", (event) => {
    event.preventDefault(); // Empêche le comportement par défaut du lien
    const imageUrl = thumbnail.getAttribute("href");
    changeMainImage(imageUrl); // Changez l'image principale avec l'URL de la miniature
  });
});

// Récupérez toutes les mini-images
const miniImages = document.querySelectorAll(".mini-image");

// Récupérez l'image principale
const mainImage = document.getElementById("mainImage");

// Ajoutez un gestionnaire d'événements à chaque mini-image
miniImages.forEach((miniImage) => {
  miniImage.addEventListener("click", () => {
    // Récupérez la source de la mini-image cliquée
    const newImageSrc = miniImage.getAttribute("src");

    // Mettez à jour la source de l'image principale avec la nouvelle source
    mainImage.setAttribute("src", newImageSrc);
  });
});

  // Sélectionnez les éléments DOM nécessaires
  const productContainer = document.querySelector(".product-container");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const productElements = document.querySelectorAll(".product");

  // Fonction pour recalculer scrollAmount en fonction de la largeur de l'écran
  function recalculateScrollAmount() {
    const windowWidth = window.innerWidth;
    const computedStyle = window.getComputedStyle(productElements[0]);
    const marginLeft = parseInt(computedStyle.marginLeft, 10);
    const marginRight = parseInt(computedStyle.marginRight, 10);
    const productWidth =
      productElements[0].offsetWidth + marginLeft + marginRight;
    return productWidth;
  }

  let scrollAmount = recalculateScrollAmount();

  let scrollPosition = 0;

  // Écoutez les événements de redimensionnement de la fenêtre
  window.addEventListener("resize", () => {
    scrollAmount = recalculateScrollAmount();
    // Vous pouvez également recalculer la position de défilement ici si nécessaire
  });

  prevBtn.addEventListener("click", () => {
    scrollPosition -= scrollAmount;
    if (scrollPosition < 0) {
      scrollPosition = 0;
    }
    productContainer.scroll({
      left: scrollPosition,
      behavior: "smooth",
    });
  });

  nextBtn.addEventListener("click", () => {
    scrollPosition += scrollAmount;
    const maxScroll = productContainer.scrollWidth - productContainer.clientWidth;
    if (scrollPosition > maxScroll) {
      scrollPosition = maxScroll;
    }
    productContainer.scroll({
      left: scrollPosition,
      behavior: "smooth",
    });
  });
