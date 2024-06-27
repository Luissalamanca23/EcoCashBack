function validarCamposContacto(event) {
    event.preventDefault();
    var nombre = $('#nombre').val();
    var email = $('#email').val();
    var mensaje = $('#mensaje').val();
    var mensaje_nombre = $('#val_nom_contac');
    var mensaje_correo = $('#val_email_contac');
    var mensaje_mensaje = $('#val_mensaje_contac');
    var mensaje_campo = $('#val_camp_msg');
    var mensaje_validar_c = $('.msg-validar-campos_cont');
    var regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

    if (nombre === '' && email === '' && mensaje === '') {
        mensaje_campo.text('Para enviar un mensaje, los campos nombre, correo y mensaje no pueden estar vacíos');
        mensaje_validar_c.css('display', 'block');
        mensaje_campo.css('color', 'white');
        mensaje_campo.css('backgroundColor', 'red');
        mensaje_campo.css('padding', '7px');
        mensaje_campo.css('borderRadius', '15px');
        mensaje_campo.css('margin-top', '10px');
        mensaje_campo.css('margin-bottom', '10px');
        setTimeout(() => {
            mensaje_campo.css('display', 'none');
        }, 3000);
    }
    else if (nombre === '') {
        mensaje_nombre.text('El campo nombre no puede estar vacío');
        mensaje_validar_c.css('display', 'block');
        mensaje_nombre.css('color', 'white');
        mensaje_nombre.css('backgroundColor', 'red');
        mensaje_nombre.css('padding', '7px');
        mensaje_nombre.css('borderRadius', '15px');
        mensaje_nombre.css('margin-top', '10px');
        mensaje_nombre.css('margin-bottom', '10px');
        setTimeout(() => {
            mensaje_nombre.css('display', 'none');
        }, 3000);
    }
    else if (email === '') {
        mensaje_correo.text('El campo correo no puede estar vacío');
        mensaje_validar_c.css('display', 'block');
        mensaje_correo.css('color', 'white');
        mensaje_correo.css('backgroundColor', 'red');
        mensaje_correo.css('padding', '7px');
        mensaje_correo.css('borderRadius', '15px');
        mensaje_correo.css('margin-top', '10px');
        mensaje_correo.css('margin-bottom', '10px');
        setTimeout(() => {
            mensaje_correo.css('display', 'none');
        }, 3000);
    }
    else if (!regex.test(email)) {
        mensaje_correo.text('El formato de correo no es válido');
        mensaje_validar_c.css('display', 'block');
        mensaje_correo.css('color', 'white');
        mensaje_correo.css('backgroundColor', 'red');
        mensaje_correo.css('padding', '7px');
        mensaje_correo.css('borderRadius', '15px');
        mensaje_correo.css('margin-top', '10px');
        mensaje_correo.css('margin-bottom', '10px');
        setTimeout(() => {
            mensaje_correo.css('display', 'none');
        }, 3000);
    }
    else if (mensaje === '') {
        mensaje_mensaje.text('El campo mensaje no puede estar vacío');
        mensaje_validar_c.css('display', 'block');
        mensaje_mensaje.css('color', 'white');
        mensaje_mensaje.css('backgroundColor', 'red');
        mensaje_mensaje.css('padding', '7px');
        mensaje_mensaje.css('borderRadius', '15px');
        mensaje_mensaje.css('margin-top', '10px');
        mensaje_mensaje.css('margin-bottom', '10px');
        setTimeout(() => {
            mensaje_mensaje.css('display', 'none');
        }, 3000);
    }
    else {
        console.log('Mensaje enviado');
        mensaje_mensaje.text('Mensaje enviado');
        mensaje_validar_c.css('display', 'block');
        mensaje_mensaje.css('color', 'white');
        mensaje_mensaje.css('backgroundColor', 'green');
        mensaje_mensaje.css('padding', '7px');
        mensaje_mensaje.css('borderRadius', '15px');
        mensaje_mensaje.css('margin-top', '10px');
        mensaje_mensaje.css('margin-bottom', '10px');
        setTimeout(() => {
            mensaje_mensaje.css('display', 'none');
        }, 3000);
    }
}

$(document).ready(function () {
    $('#btn-enviar').click(validarCamposContacto);
});