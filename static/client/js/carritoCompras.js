const btnAgregar = document.querySelectorAll('.addCarrito')
let carrito = []

btnAgregar.forEach(btn => {
    btn.addEventListener('click', addToCarritoItem);
})

function addToCarritoItem(e) {
    const talla = document.getElementById('talla').value;

    if (talla != 'Selecciona el modelo') {
        Toastify({
            text: "Producto agregado",
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

        const button = e.target
        const item = button.closest('.contenedor')
        const itemNombre = item.querySelector('#nombreProducto').textContent;
        const talla = item.querySelector('#talla');
        const itemTalla = talla.options[talla.selectedIndex].textContent;
        const itemPrecio = item.querySelector('#precioOferta').textContent;
        const itemImg = item.querySelector('#imgPrincipal').src;
        const itemCant = item.querySelector('#cantidad').value;

        const newProducto = {
            title: itemNombre,
            precio: parseFloat(itemPrecio),
            talla: itemTalla,
            color: "Azul",
            cantidad: parseInt(itemCant),
            img: itemImg,
        }

        addItemCarrito(newProducto)
    } else {
        Toastify({
            text: "Seleccione una talla",
            duration: 3000,
            close: true,
            gravity: "top", // `top` or `bottom`
            position: "right", // `left`, `center` or `right`
            stopOnFocus: true, // Prevents dismissing of toast on hover
            style: {
                background: "linear-gradient(to right, #777, #f7f5f5)",
                borderRadius: "2rem",
                textTransform: "uppercase",
                fontSize: ".75rem",
                fontWeight: "bold",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                boxShadow: "5px 5px 10px #ccc"   
            },
            offset: {
                x: '1.5rem', // horizontal axis - can be a number or a string indicating unity. eg: '2em'
                y: '1.5rem' // vertical axis - can be a number or a string indicating unity. eg: '2em'
            },
            onClick: function () { } // Callback after click
        }).showToast();
    }
}

function addItemCarrito(newProducto) {
    let productoExistente = false;
    const cantidadAgregar = parseInt(newProducto.cantidad);

    // Cargar datos existentes del localStorage
    const carritoJSON = localStorage.getItem('carrito');
    if (carritoJSON) {
        carrito = JSON.parse(carritoJSON);
    }

    for (let i = 0; i < carrito.length; i++) {
        if (carrito[i].title.trim() === newProducto.title.trim()) {
            const cant = carrito[i].cantidad;
            carrito[i].cantidad = cant + cantidadAgregar;
            productoExistente = true;
            break;
        }
    }

    if (!productoExistente) {
        carrito.push(newProducto);
    }

    addLocalStorage();
    obtenerCantidadProductosCarrito();
}

function addLocalStorage() {
    localStorage.setItem('carrito', JSON.stringify(carrito));
}

function obtenerCantidadProductosCarrito() {
    let totalCantidad = 0;

    for (let i = 0; i < carrito.length; i++) {
        totalCantidad = carrito.length;
    }

    const cantidadProductos = document.getElementById("totalCarrito");
    cantidadProductos.textContent = totalCantidad;
}

document.addEventListener('DOMContentLoaded', cargarCantidadProdCarrito);

function cargarCantidadProdCarrito() {
    // Cargar datos existentes del localStorage
    const carritoJSON = localStorage.getItem('carrito');
    if (carritoJSON) {
        carrito = JSON.parse(carritoJSON);
        obtenerCantidadProductosCarrito();
    }
}



