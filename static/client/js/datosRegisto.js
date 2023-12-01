document.getElementById("btnEnvioRegistro").addEventListener("click", function (e) {
    e.preventDefault(); // Evita la redirección por defecto

    // Obtener los valores de los campos de entrada
    const user = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const contrasena = document.getElementById("confirm-password").value;
    const nombre = document.getElementById("nombre_completo").value;
    const apePat = document.getElementById("apellido_paterno").value;
    const apeMat = document.getElementById("apellido_materno").value;
    const telf = document.getElementById("telefono").value;
    const dni = document.getElementById("docid").value;

    // Validar si se han ingresado todos los campos
    if (user === "" || email === "" || contrasena === "" || nombre === "" || apePat === "" || apeMat === "" || telf === "" || dni === "") {
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
        window.location.href = '/login';
        formulario.submit();
    }
});
