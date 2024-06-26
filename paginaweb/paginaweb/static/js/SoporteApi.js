function initMap() {
    var mapDiv = document.getElementById("map");
    var map, marker;

    // Ubicación fija (por ejemplo, la oficina de abogados "Lex")
    var fixedLocation = { lat: -34.397, lng: 150.644 };

    map = new google.maps.Map(mapDiv, {
        center: fixedLocation,
        zoom: 13
    });

    marker = new google.maps.Marker({
        position: fixedLocation,
        map: map,
        title: "Oficina de abogados 'Lex'",
        icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
        }
    });

    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'location': fixedLocation }, function(results, status) {
        if (status === 'OK') {
            if (results[0]) {
                document.getElementById('ubicacionInput').value = results[0].formatted_address;
            } else {
                document.getElementById('ubicacionInput').value = 'No se encontraron resultados';
            }
        } else {
            document.getElementById('ubicacionInput').value = 'Error en geolocalización: ' + status;
        }
    });

    function handleLocationError(browserHasGeolocation, pos) {
        var errorMessage = browserHasGeolocation ? 
                           'Error: El servicio de geolocalización ha fallado.' : 
                           'Error: Tu navegador no soporta geolocalización.';
        alert(errorMessage);
    }
}

document.addEventListener("DOMContentLoaded", function() {
    var script = document.createElement("script");
    script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyCWZRDRYSCz3oDOOBBpywKrmO962VNIJqA&callback=initMap&libraries=&v=weekly`;
    script.async = true;
    document.head.appendChild(script);
});
