let datosPago = localStorage.getItem("datosPago");

document.getElementById('linkBtnEnvio').addEventListener('click', function (event) {
    event.preventDefault(); // Evitar que se siga el enlace de forma predeterminada

    // Obtener los valores de los campos del formulario
    const nombres = document.getElementById('nombres').value;
    const apellidos = document.getElementById('apellidos').value;
    const calle = document.getElementById('calle').value;
    const departamento = document.getElementById('departamento').value;
    const provincia = document.getElementById('provincia').value;
    const distrito = document.getElementById('distrito').value;

    // Verificar si todos los campos están completos
    if (nombres === '' || apellidos === '' || calle === '' || departamento === 'Departamento' || provincia === 'Provincia' || distrito === 'Distrito') {
        // Mostrar una alerta si faltan campos
        Toastify({
            text: "Ingrese todos los datos",
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
    } else {
        actualizarDatosEnvio();
        window.location.href = 'pago.html';
    }
});

document.getElementById("linkBtnRecojo").addEventListener("click", function (e) {
    e.preventDefault(); // Evita la redirección por defecto

    // Obtener los valores de los campos de entrada
    var nombres = document.getElementById("nomRecojo").value;
    var apellidos = document.getElementById("apeRecojo").value;
    var dni = document.getElementById("docRocojo").value;

    // Validar si se han ingresado todos los campos
    if (nombres === "" || apellidos === "" || dni === "") {
        Toastify({
            text: "Ingrese todos los datos",
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
    } else {
        actualizarDatosRecojo();
        window.location.href = 'pago.html';
    }
});

function actualizarDatosEnvio() {
    var metodoEnvio = "Envio Gratis";
    var nombre = document.getElementById("nombres").value;
    var apellido = document.getElementById("apellidos").value;

    if (datosPago) {
        // Parsear los datos existentes a un objeto o arreglo
        datosPago = JSON.parse(datosPago);

        // Actualizar los valores necesarios
        datosPago.nombre = nombre;
        datosPago.apellidos = apellido;
        datosPago.metodo = metodoEnvio;
    } else {
        // Crear un nuevo objeto con los valores
        datosPago = {
            nombre: nombre,
            apellidos: apellido,
            metodo: metodoEnvio
        };
    }

    // Guardar los datos actualizados en el localStorage
    localStorage.setItem("datosPago", JSON.stringify(datosPago));
}

function actualizarDatosRecojo() {
    var metodoEnvio = "Recojo En Tienda";
    var nombre = document.getElementById("nomRecojo").value;
    var apellido = document.getElementById("apeRecojo").value;

    if (datosPago) {
        // Parsear los datos existentes a un objeto o arreglo
        datosPago = JSON.parse(datosPago);

        // Actualizar los valores necesarios
        datosPago.nombre = nombre;
        datosPago.apellidos = apellido;
        datosPago.metodo = metodoEnvio;
    } else {
        // Crear un nuevo objeto con los valores
        datosPago = {
            nombre: nombre,
            apellidos: apellido,
            metodo: metodoEnvio
        };
    }

    // Guardar los datos actualizados en el localStorage
    localStorage.setItem("datosPago", JSON.stringify(datosPago));
}

var btnCancelar = document.getElementById("white");

btnCancelar.addEventListener("click", redireccion);

function redireccion() {
    window.location.href = 'carrito.html';
}

