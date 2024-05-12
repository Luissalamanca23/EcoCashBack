function validar_email(event) {
    var email = $('#email-suscripcion').val();
    var regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    var mensaje = $('#mensaje');

    if (email.trim() === '') {
        console.log('El campo de correo electrónico está vacío');
        mensaje.text('El campo de correo electrónico no puede estar vacío');
        $('.msg-correo-sus').css('display', 'block');
        mensaje.css('backgroundColor', '#ff0000');
        event.preventDefault(); // Evita el envío del formulario si el campo de correo electrónico está vacío
        setTimeout(() => {
            $('.msg-correo-sus').css('display', 'none');
        }, 3000);
    } else if (regex.test(email)) {
        console.log('El correo electrónico es válido');
        mensaje.text('Te as suscrito correctamente a nuestro boletín');
        $('.msg-correo-sus').css('display', 'block');
        mensaje.css('backgroundColor', '#42ac25c0');
    } else {
        console.log('El correo electrónico no es válido');
        mensaje.text('El correo electrónico no es válido');
        $('.msg-correo-sus').css('display', 'block');
        mensaje.css('backgroundColor', '#ff0000');
        event.preventDefault(); // Evita el envío del formulario si el correo electrónico no es válido
        setTimeout(() => {
            $('.msg-correo-sus').css('display', 'none');
        }, 3000);
    }
    mensaje.css('display', 'inline-block');
}


$(document).ready(function () {
    $('#btn-suscribir').click(validar_email);
} );