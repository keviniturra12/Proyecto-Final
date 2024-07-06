document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll(".nav-link");
    const sections = document.querySelectorAll(".content-section");

    // Mostrar la primera sección por defecto
    sections.forEach(section => section.style.display = 'none');
    document.querySelector('.content-section').style.display = 'block';

    navLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();

            // Ocultar todas las secciones y eliminar la clase activa de todos los enlaces
            navLinks.forEach(link => link.classList.remove("active"));
            sections.forEach(section => section.style.display = 'none');

            // Mostrar la sección correspondiente y añadir la clase activa al enlace clicado
            link.classList.add("active");
            const sectionId = link.getAttribute("data-section");
            document.getElementById(sectionId).style.display = 'block';

            
    document.getElementById('rut_cliente').addEventListener('change', function() {
        const rutSelect = document.getElementById('rut_cliente');
        const nombreClienteInput = document.getElementById('nombre_cliente');
        const selectedOption = rutSelect.options[rutSelect.selectedIndex];
        const nombreCliente = selectedOption.getAttribute('data-nombre');
        nombreClienteInput.value = nombreCliente;
    });
        });
    });
});

