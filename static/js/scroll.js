// Sélectionnez les éléments DOM nécessaires pour la section "NEW PRODUCTS"
const newProductsContainer = document.querySelector(".product-container");
const prevBtnNewProducts = document.getElementById("prevBtnNewProducts");
const nextBtnNewProducts = document.getElementById("nextBtnNewProducts");
const newProductElements = document.querySelectorAll(".product");

// Sélectionnez les éléments DOM nécessaires pour la section "PROMO PRODUCTS"
const promoProductsContainer = document.querySelector(".product-container-promo");
const prevBtnPromoProducts = document.getElementById("prevBtnPromoProducts");
const nextBtnPromoProducts = document.getElementById("nextBtnPromoProducts");
const promoProductElements = document.querySelectorAll(".product-promo");

// Fonction pour recalculer scrollAmount en fonction de la largeur de l'écran
function recalculateScrollAmount(elements) {
  const windowWidth = window.innerWidth;
  const computedStyle = window.getComputedStyle(elements[0]);
  const marginLeft = parseInt(computedStyle.marginLeft, 10);
  const marginRight = parseInt(computedStyle.marginRight, 10);
  const productWidth = elements[0].offsetWidth + marginLeft + marginRight;
  return productWidth;
}

let scrollAmountNewProducts = recalculateScrollAmount(newProductElements);
let scrollAmountPromoProducts = recalculateScrollAmount(promoProductElements);

let scrollPositionNewProducts = 0;
let scrollPositionPromoProducts = 0;

// Écoutez les événements de redimensionnement de la fenêtre
window.addEventListener("resize", () => {
  scrollAmountNewProducts = recalculateScrollAmount(newProductElements);
  scrollAmountPromoProducts = recalculateScrollAmount(promoProductElements);
  // Vous pouvez également recalculer la position de défilement ici si nécessaire
});

prevBtnNewProducts.addEventListener("click", () => {
  scrollPositionNewProducts -= scrollAmountNewProducts;
  if (scrollPositionNewProducts < 0) {
    scrollPositionNewProducts = 0;
  }
  newProductsContainer.scroll({
    left: scrollPositionNewProducts,
    behavior: "smooth",
  });
});

nextBtnNewProducts.addEventListener("click", () => {
  scrollPositionNewProducts += scrollAmountNewProducts;
  const maxScroll = newProductsContainer.scrollWidth - newProductsContainer.clientWidth;
  if (scrollPositionNewProducts > maxScroll) {
    scrollPositionNewProducts = maxScroll;
  }
  newProductsContainer.scroll({
    left: scrollPositionNewProducts,
    behavior: "smooth",
  });
});

prevBtnPromoProducts.addEventListener("click", () => {
  scrollPositionPromoProducts -= scrollAmountPromoProducts;
  if (scrollPositionPromoProducts < 0) {
    scrollPositionPromoProducts = 0;
  }
  promoProductsContainer.scroll({
    left: scrollPositionPromoProducts,
    behavior: "smooth",
  });
});

nextBtnPromoProducts.addEventListener("click", () => {
  scrollPositionPromoProducts += scrollAmountPromoProducts;
  const maxScroll = promoProductsContainer.scrollWidth - promoProductsContainer.clientWidth;
  if (scrollPositionPromoProducts > maxScroll) {
    scrollPositionPromoProducts = maxScroll;
  }
  promoProductsContainer.scroll({
    left: scrollPositionPromoProducts,
    behavior: "smooth",
  });
});
