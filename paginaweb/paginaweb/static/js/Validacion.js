document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("formularioRegistro");

    // Validaciones de campos
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        
        let isValid = true;
        
        // Validación del nombre
        const nombre = document.getElementById("first_name");
        const errorNombre = document.getElementById("errorFirstName");
        if (nombre.value.length < 10) {
            isValid = false;
            errorNombre.style.display = "block";
        } else {
            errorNombre.style.display = "none";
        }

        // Validación del RUT
        const rut = document.getElementById("rut");
        const errorRut = document.getElementById("errorRut");
        const rutRegex = /^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$/;
        if (!rutRegex.test(rut.value)) {
            isValid = false;
            errorRut.style.display = "block";
        } else {
            errorRut.style.display = "none";
        }

        // Validación de la dirección
        const direccion = document.getElementById("address");
        const errorDireccion = document.getElementById("errorAddress");
        if (direccion.value.length < 10) {
            isValid = false;
            errorDireccion.style.display = "block";
        } else {
            errorDireccion.style.display = "none";
        }

        // Validación del correo electrónico
        const email = document.getElementById("email");
        const errorEmail = document.getElementById("errorEmail");
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value)) {
            isValid = false;
            errorEmail.style.display = "block";
        } else {
            errorEmail.style.display = "none";
        }

        // Validación del teléfono
        const phone = document.getElementById("phone");
        const errorPhone = document.getElementById("errorPhone");
        const phoneRegex = /^\d{9,}$/;
        if (!phoneRegex.test(phone.value)) {
            isValid = false;
            errorPhone.style.display = "block";
        } else {
            errorPhone.style.display = "none";
        }

        // Validación de la fecha de nacimiento
        const fechaNacimiento = document.getElementById("date_of_birth");
        const errorFechaNacimiento = document.getElementById("errorDateOfBirth");
        if (!fechaNacimiento.value) {
            isValid = false;
            errorFechaNacimiento.style.display = "block";
        } else {
            errorFechaNacimiento.style.display = "none";
        }

        // Validación de la contraseña
        const password = document.getElementById("password");
        const errorPassword = document.getElementById("errorPassword");
        if (password.value.length < 6) { // Ejemplo: longitud mínima de 6 caracteres
            isValid = false;
            errorPassword.style.display = "block";
        } else {
            errorPassword.style.display = "none";
        }

        // Validación de la confirmación de contraseña
        const confirmPassword = document.getElementById("confirm_password");
        const errorConfirmPassword = document.getElementById("errorConfirmPassword");
        if (confirmPassword.value !== password.value) {
            isValid = false;
            errorConfirmPassword.style.display = "block";
        } else {
            errorConfirmPassword.style.display = "none";
        }

        // Mostrar mensaje de error o éxito
        const mensajeError = document.getElementById("mensajeError");
        const mensajeExito = document.getElementById("mensajeExito");
        if (!isValid) {
            mensajeError.style.display = "block";
            mensajeExito.style.display = "none";
        } else {
            mensajeError.style.display = "none";
            mensajeExito.style.display = "block";
            form.submit(); // Enviar el formulario si todo es válido
        }
    });
});
