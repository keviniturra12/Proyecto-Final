document.addEventListener('DOMContentLoaded', function() {
    // Establecer la fecha preferida a la fecha actual en formato dd/mm/yyyy
    var fechaPreferida = document.getElementById('fechaPreferida');
    var today = new Date();
    var day = String(today.getDate()).padStart(2, '0');
    var month = String(today.getMonth() + 1).padStart(2, '0'); // Enero es 0
    var year = today.getFullYear();
    var formattedDate = day + '/' + month + '/' + year;
    
    // Mostrar la fecha en formato dd/mm/yyyy en el input como texto no editable
    fechaPreferida.value = formattedDate;

        // Manejar la validación de archivos en el frontend
        var archivoAdjunto = document.getElementById('archivoAdjunto');
        archivoAdjunto.addEventListener('change', function() {
            var file = this.files[0];
            var allowedExtensions = /(\.doc|\.pdf|\.exe)$/i;
            if (!allowedExtensions.exec(file.name)) {
                alert('Solo se permiten archivos .doc, .pdf o .exe');
                this.value = '';
                return false;
            }
        });
    
        // Validación adicional en el formulario si es necesario
        var form = document.getElementById('solicitudServicioForm');
        form.addEventListener('submit', function(event) {
            // Aquí puedes añadir validaciones adicionales si es necesario
        });
});