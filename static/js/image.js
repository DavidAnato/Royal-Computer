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
  