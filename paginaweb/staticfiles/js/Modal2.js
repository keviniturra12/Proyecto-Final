document.addEventListener("DOMContentLoaded", function() {
  // Get the modal element
  var modal = document.getElementById("climaModal");

  // Get the button that opens the modal
  var btn = document.getElementById("consultarClima");

  // Get the <span> element that closes the modal
  var span = document.querySelector(".btn-close");

  // When the user clicks on the button, open the modal
  if (btn) {
      btn.onclick = function() {
          modal.style.display = "block";
      }
  }

  // When the user clicks on <span> (x), close the modal
  if (span) {
      span.onclick = function() {
          modal.style.display = "none";
      }
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }
  
  // Close modal when clicking "Cerrar" button inside the modal
  var closeButton = document.querySelector("#climaModal .btn-secondary");
  if (closeButton) {
      closeButton.addEventListener("click", function() {
          modal.style.display = "none";
      });
  }
});