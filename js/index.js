function validarEmail(email) {
    var regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    return regex.test(email);
}

document.getElementById('email-suscripcion').addEventListener('input', function() {
    var email = this.value;
    if (validarEmail(email)) {
        console.log('🫡 Ahora resiviras correos electrónicos de nosotros');
    } else {
        console.log('El correo electrónico no es válido');
    }
});