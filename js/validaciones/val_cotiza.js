function validar_formulario(event) {
    
    var nombre = $('#nombre-cotiza').val();
    var email = $('#email-cotiza').val();
    var telefono = $('#telefono-cotiza').val();
    var materiales = $('#materiales-cotiza').val();
    var mensaje2 = $('#mensaje2');
    var regexEmail = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/; // Formato de correo electrónico
    var regexTelefono = /^\+569 \d{4} \d{4}$/; // Formato de teléfono: +569 1234 5678

    if (nombre === '' || email === '' || telefono === '' || materiales === '') {
        mensaje2.text('Todos los campos son obligatorios');
        mensaje2.css('backgroundColor', '#ff0000');
        $('.msg-validar-campos').css('display', 'block');
        setTimeout(() => {
            $('.msg-validar-campos').css('display', 'none');
        }, 3000);
        event.preventDefault();
    } else if (!regexEmail.test(email)) {
        mensaje2.text('El correo electrónico no es válido');
        mensaje2.css('backgroundColor', '#ff0000');
        $('.msg-validar-campos').css('display', 'block');
        setTimeout(() => {
            $('.msg-validar-campos').css('display', 'none');
        }, 3000);
        event.preventDefault();
    } else if (!regexTelefono.test(telefono)) {
        mensaje2.text('El formato del teléfono no es válido');
        mensaje2.css('backgroundColor', '#ff0000');
        $('.msg-validar-campos').css('display', 'block');
        setTimeout(() => {
            $('.msg-validar-campos').css('display', 'none');
        }, 3000);
        event.preventDefault();
    } else {
        mensaje2.text('Formulario enviado correctamente');
        mensaje2.css('backgroundColor', '#42ac25c0');
        $('.msg-validar-campos').css('display', 'block');
        setTimeout(() => {
            $('.msg-validar-campos').css('display', 'none');
        }, 3000);
    }
    mensaje2.css('display', 'inline-block');
}



$(document).ready(function () {
    $('#btn-cotizar').click(validar_formulario);
} );