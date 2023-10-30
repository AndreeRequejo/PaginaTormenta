let datosPago = localStorage.getItem("datosPago");
datosPago = JSON.parse(datosPago);
let productosEnCarrito = localStorage.getItem("carrito");
productosEnCarrito = JSON.parse(productosEnCarrito);

function cargarProductosCarrito() {
    var cartContainer = document.getElementById('productosPago');


    productosEnCarrito.forEach(item => {
        const cardElement = document.createElement('div');
        cardElement.className = 'carrito d-flex justify-content-between mb-4 gap-4';

        cardElement.innerHTML = `
            <div class="img">
                            <img src=${item.img}
                                alt="">
                        </div>
                        <div class="detallePrenda w-100">
                            <h5 id="nombre">${item.title}</h5>
                            <span id="cantidad">x${item.cantidad},</span>
                            <span id="color"> ${item.color},</span>
                            <span id="size"> ${item.talla}</span>
                        </div>
                        <div class="costo d-flex align-items-center">
                            <span id="simbolo">S/ </span>
                            <span id="precio">${item.precio}</span>
                        </div>
        `;
        cartContainer.append(cardElement);
    });

}

cargarProductosCarrito();

function cargarDatosPago() {
    var cartContainer = document.getElementsByClassName('resumen');
    var montoSubTotal = 0;

    productosEnCarrito.forEach(item => {
        montoSubTotal += item.precio * item.cantidad;
    });

    var montoTotal = (montoSubTotal-datosPago.desc).toFixed(2);

    const cardElement = document.createElement('div');
    cardElement.className = 'container px-5';
    cardElement.innerHTML = `
        <div class="d-flex justify-content-between align-items-center">
            <h4 class="totales">Sub Total</h4>
            <p class="totales">S/ ${montoSubTotal}</p>
        </div>

        <div class="d-flex justify-content-between align-items-center mt-1">
            <h4 class="ite2">Envío</h4>
            <p class="m-0 ite2">S/-0</p>
        </div>

        <div class="d-flex justify-content-between align-items-center mt-1">
            <h4 class="ite2">Código Promocional</h4>
            <p class="m-0 ite2">S/-${datosPago.desc}</p>
        </div>

        <hr>

        <div class="mt-3">
            <div class="d-flex justify-content-between align-items-center">
                <h2 class="totales fs-4">Total</h2>
                <p class="totales">S/${montoTotal}</p>
            </div>
        </div>
        <div class="d-flex justify-content-center align-items-center btnPago mt-4">
            <button type="button" id="pagar">REALIZAR PAGO</button>
        </div>
        `;
    
    cartContainer[0].append(cardElement);
}

cargarDatosPago();

document.getElementById('pagar').addEventListener('click', function (event) {
    event.preventDefault();

    const metodoSeleccionado = document.querySelector('input[name="flexRadioDefault"]:checked').id;

    if (metodoSeleccionado === 'tarjetaCred') {
        const numTarjeta = document.getElementById('numTarjeta').value;
        const tiempo = document.getElementById('tiempo').value;
        const cvc = document.getElementById('cvc').value;
        const documento = document.getElementById('documento').value;
        const tipoDoc = document.getElementById('tipoDoc').value;

        if (numTarjeta === '' || tiempo === '' || cvc === '' || documento === '' || tipoDoc === 'Tipo de Documento') {
            Toastify({
                text: "Complete los datos de pago",
                duration: 3000,
                close: true,
                gravity: "top",
                position: "right",
                stopOnFocus: true,
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
                    x: '1.5rem',
                    y: '1.5rem'
                },
                onClick: function () { }
            }).showToast();
        }
    } else {
        agregarAnimacionPago();
        var nombrePago = document.getElementById('personaPago');
        nombrePago.textContent = datosPago.nombre + ' ' + datosPago.apellidos;
		localStorage.clear();
    }
});

function agregarAnimacionPago() {
    var btnPagar = document.getElementById('pagar');
    btnPagar.setAttribute('data-bs-toggle', 'modal');
    btnPagar.setAttribute('data-bs-target', '#modalPago');

    btnPagar.click();
}