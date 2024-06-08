document.addEventListener("DOMContentLoaded", function() {
    // Get the modal element
    var modal = document.getElementById("climaModal");

    // Get the button that opens the modal
    var btn = document.getElementById("consultarClima");

    // Get the <span> element that closes the modal
    var span = document.querySelector(".btn-close");

    // When the user clicks on the button, open the modal
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
    
    // Close modal when clicking "Cerrar" button inside the modal
    var closeButton = document.querySelector("#climaModal .btn-secondary");
    closeButton.addEventListener("click", function() {
        modal.style.display = "none";
    });

    
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var usuario = document.getElementById('username').value.trim();
    var contraseña = document.getElementById('password').value.trim();

    var errorUsuario = document.getElementById('errorUsuario');
    var errorContraseña = document.getElementById('errorContraseña');
    var mensajeExito = document.getElementById('mensajeExito');
    var mensajeError = document.getElementById('mensajeError');

    // Resetear mensajes de error y éxito
    errorUsuario.textContent = '';
    errorUsuario.style.display = 'none';
    errorContraseña.textContent = '';
    errorContraseña.style.display = 'none';
    mensajeExito.style.display = 'none';
    mensajeError.style.display = 'none';

    // Validar contraseña
    if (contraseña.length < 10) {
      errorContraseña.textContent = 'La contraseña debe tener al menos 10 caracteres.';
      errorContraseña.style.display = 'block';
    }

    // Validar correo
    var usuarioRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!usuarioRegex.test(usuario)) {
      errorUsuario.textContent = 'Usuario inválido.';
      errorUsuario.style.display = 'block';
    }

    // Verificar si hay algún error
    if (errorUsuario.textContent || errorContraseña.textContent) {
      mensajeError.style.display = 'block';
      return; // Si hay errores, no enviar el formulario
    }

    // Si no hay errores, mostrar mensaje de éxito y resetear el formulario
    mensajeExito.style.display = 'block';
    document.getElementById('loginForm').reset();
  });