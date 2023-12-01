document.getElementById("btnInicioSesion").addEventListener("click", function (e) {
    e.preventDefault(); // Evita la redirección por defecto

    // Obtener los valores de los campos de entrada
    const user = document.getElementById("username").value;
    const contrasena = document.getElementById("password").value;

    // Validar si se han ingresado todos los campos
    if (user === "" || contrasena === "") {
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
        formulario.submit();
    }
});