document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("formularioRegistro");
    const mensajeError = document.getElementById("mensajeError");
    const mensajeExito = document.getElementById("mensajeExito");

    form.addEventListener("submit", function(event) {
        let valid = true;
        mensajeError.style.display = "none";
        mensajeExito.style.display = "none";

        // Limpia los errores previos
        const errorElements = document.querySelectorAll(".invalid-feedback");
        errorElements.forEach(el => el.style.display = "none");

        // Validación de RUT
        const rut = form.rut_cliente.value;
        if (!validarRut(rut)) {
            mostrarError("rut_cliente", "RUT inválido");
            valid = false;
        }

        // Validación de correo electrónico
        const email = form.correo_electronico.value;
        if (!validarEmail(email)) {
            mostrarError("correo_electronico", "Correo electrónico inválido");
            valid = false;
        }

        // Validación de contraseña
        const password = form.password.value;
        const confirmPassword = form.confirm_password.value;
        if (password !== confirmPassword) {
            mostrarError("confirm_password", "Las contraseñas no coinciden");
            valid = false;
        }

        if (!valid) {
            event.preventDefault();
            mensajeError.style.display = "block";
        } else {
            mensajeExito.style.display = "block";
        }
    });

    function mostrarError(id, message) {
        const input = document.getElementById(id);
        const errorDiv = input.nextElementSibling;
        errorDiv.textContent = message;
        errorDiv.style.display = "block";
    }

    function validarRut(rut) {
        // Implementa la validación de RUT
        return true; // Placeholder
    }

    function validarEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }
});
