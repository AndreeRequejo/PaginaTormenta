function obtenerCantidadProductosCarrito() {
    let totalCantidad = 0;

    for (let i = 0; i < productosEnCarrito.length; i++) {
        totalCantidad = productosEnCarrito.length;
    }

    const cantidadProductos = document.getElementById("totalCarrito");
    const prodEnCarro = document.getElementById("ProdEnCarro");
    cantidadProductos.textContent = totalCantidad;
}

document.addEventListener('DOMContentLoaded', cargarCantidadProdCarrito);

function cargarCantidadProdCarrito() {
    // Cargar datos existentes del localStorage
    const carritoJSON = localStorage.getItem('carrito');
    if (carritoJSON) {
        productosEnCarrito = JSON.parse(carritoJSON);
        obtenerCantidadProductosCarrito();
    }
}


function scrollToTop() {
    window.scrollTo(0, 0); // Desplaza la página a la posición (0, 0)
}

// Evento que se dispara cuando la página se carga/reinicia
window.onload = function () {
    scrollToTop(); // Desplaza la página hacia arriba al cargarse/reiniciarse
};


function toggleCurrentPassword() {
    const passwordInput = document.getElementById('currentPassword');
    const toggleButton = document.getElementById('toggleCurrentPassword');
    const hiddenIcon = document.getElementById('toggleCurrentPasswordHidden');

    const isPasswordVisible = passwordInput.type === 'text';

    passwordInput.type = isPasswordVisible ? 'password' : 'text';
    toggleButton.className = isPasswordVisible ? 'icon-eye bx bxs-low-vision rounded' : 'icon-eye bx bx-low-vision rounded';
    hiddenIcon.hidden = !isPasswordVisible;
  }

  function toggleNewPassword() {
    const passwordInput = document.getElementById('newPassword');
    const toggleButton = document.getElementById('toggleNewPassword');
    const hiddenIcon = document.getElementById('toggleNewPasswordHidden');

    const isPasswordVisible = passwordInput.type === 'text';

    passwordInput.type = isPasswordVisible ? 'password' : 'text';
    toggleButton.className = isPasswordVisible ? 'icon-eye bx bxs-low-vision rounded' : 'icon-eye bx bx-low-vision rounded';
    hiddenIcon.hidden = !isPasswordVisible;
  }