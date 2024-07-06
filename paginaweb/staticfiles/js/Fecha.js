document.addEventListener('DOMContentLoaded', function () {
    const fechaRegistro = document.getElementById('fechaRegistro');
    const today = new Date();
    const date = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
    fechaRegistro.value = date;
});
