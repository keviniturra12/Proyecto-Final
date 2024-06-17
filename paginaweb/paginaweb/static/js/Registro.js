document.getElementById('formularioContacto').addEventListener('submit', function(event) {
    event.preventDefault();

    var nombre = document.getElementById('nombre').value.trim();
    var correo = document.getElementById('correo').value.trim();
    var tipoProducto = document.getElementById('tipoProducto').value.trim();
    var asunto = document.getElementById('asunto').value.trim();
    var mensaje = document.getElementById('mensaje').value.trim();

    var errorNombre = document.getElementById('errorNombre');
    var errorCorreo = document.getElementById('errorCorreo');
    var errorTipoProducto = document.getElementById('errorTipoProducto');
    var errorAsunto = document.getElementById('errorAsunto');
    var errorMensaje = document.getElementById('errorMensaje');
    var mensajeExito = document.getElementById('mensajeExito');
    var mensajeError = document.getElementById('mensajeError');

    // Resetear mensajes de error y éxito
    errorNombre.textContent = '';
    errorCorreo.textContent = '';
    errorTipoProducto.textContent = '';
    errorAsunto.textContent = '';
    errorMensaje.textContent = '';
    mensajeExito.style.display = 'none';
    mensajeError.style.display = 'none';

    // Validar nombre
    if (nombre.length < 10) {
      errorNombre.textContent = 'El nombre debe tener al menos 10 caracteres*.';
    }

    // Validar correo
    var correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!correoRegex.test(correo)) {
      errorCorreo.textContent = 'Correo electrónico inválido*.';
    }

    // Validar tipo de producto
    if (tipoProducto.length === 0) {
      errorTipoProducto.textContent = 'Este campo es obligatorio*.';
    }

    // Validar asunto
    if (asunto.length === 0) {
      errorAsunto.textContent = 'Este campo es obligatorio*.';
    }

    // Validar mensaje
    if (mensaje.length < 10 ) {
      errorMensaje.textContent = 'El nombre debe tener al menos 10 caracteres*.';
      
    }

    // Verificar si hay algún error
    if (errorNombre.textContent || errorCorreo.textContent || errorTipoProducto.textContent || errorAsunto.textContent || errorMensaje.textContent) {
      return; // Si hay errores, no enviar el formulario
    }

    // Si no hay errores, mostrar mensaje de éxito y resetear el formulario
    mensajeExito.style.display = 'block';
    document.getElementById('formularioContacto').reset();
  });
