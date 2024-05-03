
// validar email y que tenga formato de email


function validar_email(event) {
    event.preventDefault();
    var email = $('#email-suscripcion').val();
    var regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    var mensaje = $('#mensaje');

    if (regex.test(email)) {
        console.log('El correo electrónico es válido');
        mensaje.text('Te as suscrito correctamente a nuestro boletín');
        mensaje.css('backgroundColor', '#42ac25c0');
    } else {
        console.log('El correo electrónico no es válido');
        mensaje.text('El correo electrónico no es válido o está vacío');
        mensaje.css('backgroundColor', '#ff0000');
    }
    mensaje.css('display', 'inline-block');
}


// validar formulario de cotización y que todos los campos estén llenos
function validar_formulario(event) {
    event.preventDefault();
    var nombre = $('#nombre-cotiza').val();
    var email = $('#email-cotiza').val();
    var telefono = $('#telefono-cotiza').val();
    var materiales = $('#materiales-cotiza').val();
    var mensaje2 = $('#mensaje2');
    var regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;

    if (nombre === '' || email === '' || telefono === '' || materiales === '') {
        mensaje2.text('Todos los campos son obligatorios');
        mensaje2.css('backgroundColor', '#ff0000');
    } else if (!regex.test(email)) {
        mensaje2.text('El correo electrónico no es válido');
        mensaje2.css('backgroundColor', '#ff0000');
    } else {
        mensaje2.text('Formulario enviado correctamente');
        mensaje2.css('backgroundColor', '#42ac25c0');
    }
    mensaje2.css('display', 'inline-block');
}




$(document).ready(function () {
    $('#btn-suscribir').click(validar_email);
    $('#btn-cotizar').click(validar_formulario);
} );