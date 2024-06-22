function initMap() {
    var mapDiv = document.getElementById("map");
    var map, marker;

    map = new google.maps.Map(mapDiv, {
        center: {lat: -34.397, lng: 150.644},
        zoom: 13
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                var pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };

                map.setCenter(pos);

                marker = new google.maps.Marker({
                    position: pos,
                    map: map,
                    title: "Ubicación encontrada",
                    icon: {
                        url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                    }
                });

                var geocoder = new google.maps.Geocoder();
                geocoder.geocode({ 'location': pos }, function(results, status) {
                    if (status === 'OK') {
                        if (results[0]) {
                            ubicacionInput.value = results[0].formatted_address;
                        } else {
                            ubicacionInput.value = 'No se encontraron resultados';
                        }
                    } else {
                        ubicacionInput.value = 'Error en geolocalización: ' + status;
                    }
                });
            },
            function() {
                handleLocationError(true, map.getCenter());
            }
        );
    } else {
        handleLocationError(false, map.getCenter());
    }

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
