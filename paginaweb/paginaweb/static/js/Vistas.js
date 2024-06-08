document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll(".nav-link");
    const sections = document.querySelectorAll(".content-section");

    navLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();

            // Remove active class from all links and sections
            navLinks.forEach(link => link.classList.remove("active"));
            sections.forEach(section => section.classList.remove("active"));

            // Add active class to the clicked link and the corresponding section
            link.classList.add("active");
            const sectionId = link.getAttribute("data-section");
            document.getElementById(sectionId).classList.add("active");
        });
    });
});