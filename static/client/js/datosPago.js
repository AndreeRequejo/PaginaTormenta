let datosPago = localStorage.getItem("datosPago");
datosPago = JSON.parse(datosPago);
let productosEnCarrito = localStorage.getItem("carrito");
productosEnCarrito = JSON.parse(productosEnCarrito);

function cargarProductosCarrito() {
    var cartContainer = document.getElementById('productosPago');

    productosEnCarrito.forEach((item, index) => {
        const cardElement = document.createElement('div');
        cardElement.className = 'carrito d-flex justify-content-between mb-4 gap-4';

        cardElement.innerHTML = `
            <div class="img">
                <img src=${item.img} alt="">
            </div>
            <div class="detallePrenda w-100">
                <h5 id="nombre">${item.title}</h5>
                <input type="hidden" name="producto_${index}_nomPrenda" value="${item.title}">
                <span id="cantidad">x${item.cantidad},</span>
                <input type="hidden" name="producto_${index}_cantidad" value="${item.cantidad}">
                <span id="color"> ${item.color},</span>
                <input type="hidden" name="producto_${index}_talla" value="${item.talla}">
                <input name="talla" hidden value=${item.talla} id="talla"></input>
            </div>
            <div class="costo d-flex align-items-center">
                <span id="simbolo">S/ </span>
                <span id="precio">${item.precio}</span>
                <input type="hidden" name="producto_${index}_precio" value="${item.precio}">
            </div>
        `;
        cartContainer.append(cardElement);
    });

    const cantidadProductosInput = document.createElement('input');
    cantidadProductosInput.type = 'hidden';
    cantidadProductosInput.name = 'cantidad_productos';
    cantidadProductosInput.value = productosEnCarrito.length;
    cartContainer.append(cantidadProductosInput);
}

cargarProductosCarrito();

function cargarDatosPago() {
    var cartContainer = document.getElementsByClassName('resumen');
    var montoSubTotal = 0;

    productosEnCarrito.forEach(item => {
        montoSubTotal += item.precio * item.cantidad;
    });

    var montoTotal = (montoSubTotal - datosPago.desc).toFixed(2);

    const cardElement = document.createElement('div');
    cardElement.className = 'container px-5';
    cardElement.innerHTML = `
        <div class="d-flex justify-content-between align-items-center">
            <h4 class="totales">Sub Total</h4>
            <p class="totales">S/${montoSubTotal}</p>
        </div>

        <div class="d-flex justify-content-between align-items-center mt-1">
            <h4 class="ite2">Envío</h4>
            <p class="m-0 ite2">S/-0</p>
        </div>

        <div class="d-flex justify-content-between align-items-center mt-1">
            <h4 class="ite2">Código Promocional</h4>
            <p class="m-0 ite2" id="descuento">S/-${datosPago.desc}</p>
            <input name="descuento" hidden value=${datosPago.desc} id="descuento"></input>
        </div>

        <hr>

        <div class="mt-3">
            <div class="d-flex justify-content-between align-items-center">
                <h2 class="totales fs-4">Total</h2>
                <p class="totales">S/${montoTotal}</p>
                <input name="monto_total" hidden value=${montoTotal} id="monto_total"></input>
            </div>
        </div>
        <div class="d-flex justify-content-center align-items-center btnPago mt-4">
            <button type="summit" id="pagar">REALIZAR PAGO</button>
        </div>
        `;

    cartContainer[0].append(cardElement);
}

cargarDatosPago();

document.getElementById('pagar').addEventListener('click', function (event) {
    //event.preventDefault();

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

document.addEventListener("DOMContentLoaded", function () {
    // Obtener todos los elementos con la clase "comprobante"
    var comprobanteButtons = document.querySelectorAll('.comprobante');

    // Crear un nuevo input oculto
    var nuevoInput = document.createElement('input');
    nuevoInput.type = 'hidden';
    nuevoInput.name = 'valor_comprobante_dinamico';
    nuevoInput.id = 'valor_comprobante_dinamico';
    document.getElementById('monto_total').after(nuevoInput);

    // Función para actualizar el valor del input y almacenar en localStorage
    function actualizarValorComprobante(valor) {
        // Actualizar el valor del input
        var valorComprobanteInput = document.getElementById('valor_comprobante_dinamico');
        if (valorComprobanteInput) {
            valorComprobanteInput.value = valor;
        } else {
            console.error("No se encontró el elemento con id 'valor_comprobante_dinamico'");
        }

        console.log("Value actualizado:", valorComprobanteInput.value);
    }

    // Agregar un evento de clic a cada botón
    comprobanteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Obtener el valor del botón clickeado
            var valorComprobante = button.parentElement.querySelector('.titulo_check').textContent.trim();

            // Llamar a la función para actualizar el valor
            actualizarValorComprobante(valorComprobante);
        });
    });
});