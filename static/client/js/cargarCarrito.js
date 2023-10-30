let productosEnCarrito = localStorage.getItem("carrito");
productosEnCarrito = JSON.parse(productosEnCarrito);

function cargarProductosCarrito() {

    var cartContainer = document.getElementById('detalleCarrito');
    var cartResumen = document.getElementById('resumen');
    var cartCodigo = document.getElementById('codPromocional');

    if (productosEnCarrito && productosEnCarrito.length > 0) {
        cartResumen.classList.remove('visually-hidden');
        cartCodigo.classList.remove('visually-hidden');


        productosEnCarrito.forEach(item => {
            const cardElement = document.createElement('div');
            cardElement.className = 'card mb-3 mt-5';
            cardElement.style.maxWidth = '700px';
            cardElement.style.border = 'none';

            cardElement.innerHTML = `
            <div class="row g-0">
                <div class="col-md-4"  style="width: 33%;">
                    <img src=${item.img} class="img-fluid rounded-start imgProd" alt="...">
                </div>
                <div class="col-md-8 d-flex align-items-center"  style="width: 67%;">
                    <div class="card-body">
                        <div class="d-flex align-items-center justify-content-between">
                            <h5 class="card-title" class="title">${item.title}</h5>
                            <i class='bx bxs-trash-alt'></i>
                        </div>
                        <p class="card-text"><small class="text-muted"><span class="color">${item.color}</span>, <span class="size">${item.talla}</span></small></p>
                        <div class="d-flex align-items-center justify-content-between">
                            <input type="number" class="selec-cant canti" value=${item.cantidad} min="1">
                            <div class="text-end def-cant-pre-prod">
                                <p class="m-0">S/ <span class="price">${item.precio}<span/></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

            cartContainer.append(cardElement);
        });
        actualizarBotonesEliminar();
        sumarMontosProducto();
    } else {
        cartResumen.classList.add('visually-hidden');
        cartCodigo.classList.add('visually-hidden');

        const cardVacio = document.createElement('div');
        cardVacio.className = 'd-flex justify-content-center align-items-center gap-2';
        cardVacio.style.height = '300px';
        cardVacio.innerHTML = `
            <div class="d-flex justify-content-center align-items-center gap-2" style="height: 300px;">
                <h4 class="fs-3">No hay productos en el carrito</h4>
                <i class="fa-regular fa-face-frown fs-3"></i>
            </div>
        `;

        cartContainer.append(cardVacio);
    }

}

document.addEventListener('DOMContentLoaded', function () {
    cargarProductosCarrito();
});

function obtenerCantidadProductosCarrito() {
    let totalCantidad = 0;

    for (let i = 0; i < productosEnCarrito.length; i++) {
        totalCantidad = productosEnCarrito.length;
    }

    const cantidadProductos = document.getElementById("totalCarrito");
    const prodEnCarro = document.getElementById("ProdEnCarro");
    cantidadProductos.textContent = totalCantidad;
    prodEnCarro.textContent = totalCantidad;
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

const btnDscto = document.querySelectorAll("#btn-dscto");
let dscto = 0;
btnDscto.forEach(btn => {
    btn.addEventListener('click', function () {
        dscto = calcularDescuento();
        sumarMontosProducto()
    });
});

function calcularDescuento() {
    const inpDscto = document.getElementById("inp-dscto");
    const codigoPromocional = 'G001'

    if (inpDscto.value === codigoPromocional) {
        return 0.25;
    }
}

function sumarMontosProducto() {
    const subtotal = document.getElementById("subtotal");
    const descuento = document.getElementById("descuento");
    const importe = document.getElementById("total");

    let importeSub = 0;
    let importeTotal = 0;

    for (let i = 0; i < productosEnCarrito.length; i++) {
        const cantidad = parseInt(productosEnCarrito[i].cantidad);
        const precio = parseFloat(productosEnCarrito[i].precio);

        importeSub += cantidad * precio;
    }

    importeTotal = importeSub - parseFloat(dscto) * importeSub;

    subtotal.textContent = importeSub.toFixed(2);
    descuento.textContent = (parseFloat(dscto) * importeSub).toFixed(2);
    importe.textContent = importeTotal.toFixed(2);
}

function actualizarBotonesEliminar() {
    botonesEliminar = document.querySelectorAll(".bxs-trash-alt");

    botonesEliminar.forEach(boton => {
        boton.addEventListener("click", eliminarDelCarrito);
    });
}

var cartContainer = document.getElementById("detalleCarrito");

function eliminarDelCarrito(event) {
    Toastify({
        text: "Producto eliminado",
        duration: 3000,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "right", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: "linear-gradient(to right, #717fe0, #f7f5f5)",
            borderRadius: "2rem",
            textTransform: "uppercase",
            fontSize: ".75rem",
            display: "flex",
            fontWeight: "bold",
            justifyContent: "center",
            alignItems: "center"
        },
        offset: {
            x: '1.5rem', // horizontal axis - can be a number or a string indicating unity. eg: '2em'
            y: '1.5rem' // vertical axis - can be a number or a string indicating unity. eg: '2em'
        },
        onClick: function () { } // Callback after click
    }).showToast();

    var btnDelete = event.target;
    var cardElement = btnDelete.closest(".card");
    var index = Array.from(cartContainer.children).indexOf(cardElement);
    productosEnCarrito.splice(index, 1); // Removemos el objeto del arreglo del carrito
    cartContainer.innerHTML = "";
    cargarProductosCarrito();
    localStorage.setItem('carrito', JSON.stringify(productosEnCarrito)); 
    sumarMontosProducto();
    cargarCantidadProdCarrito();
}

cartContainer.addEventListener("change", actualizarCantProductos);

function actualizarCantProductos(event) {
    var inputCant = event.target;
    if (inputCant.classList.contains("selec-cant", "canti")) {
        var nuevaCantidad = parseInt(inputCant.value);
        var cardElement = inputCant.closest(".card");
        var index = Array.from(cartContainer.children).indexOf(cardElement);

        // Actualizar la cantidad en el objeto correspondiente en el arreglo productosEnCarrito
        productosEnCarrito[index].cantidad = nuevaCantidad;

        // Actualizar el localStorage con los cambios
        localStorage.setItem('carrito', JSON.stringify(productosEnCarrito));
    }
    sumarMontosProducto()
}

var btnPagar = document.getElementById("btnPagar");
btnPagar.addEventListener("click", agregarDatosPago);

function agregarDatosPago() {
    var descuento = document.getElementById("descuento");
    const datosPago = {
        nombre: "",
        apellidos: "",
        metodo: "",
        desc: parseFloat(descuento.textContent),
    }

    localStorage.setItem('datosPago', JSON.stringify(datosPago));
}