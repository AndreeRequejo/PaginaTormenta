function scrollToTop() {
    window.scrollTo(0, 0); // Desplaza la página a la posición (0, 0)
  }

  // Evento que se dispara cuando la página se carga/reinicia
  window.onload = function() {
    scrollToTop(); // Desplaza la página hacia arriba al cargarse/reiniciarse
  };