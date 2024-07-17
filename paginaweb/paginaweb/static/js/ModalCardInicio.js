
// Función para abrir la modal con el texto correspondiente
function openModal(service, info) {
    var modal = document.getElementById("modal");
    var modalText = document.getElementById("modal-text");
    modal.style.display = "block";
    modalText.innerHTML = "<h2>" + service + "</h2><p>" + info + "</p>";
  }
  
  
  // Función para cerrar la modal
  function closeModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
  }
  
  // Función para cerrar la modal al hacer clic fuera de ella
  window.onclick = function(event) {
    var modal = document.getElementById("modal");
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
  