function validar_campos_contacto(event) {
    event.preventDefault();
    var nombre = $('#nombre').val();
    var email = $('#email').val();
    var mensaje = $('#mensaje').val();

    if (nombre === '' && email === '') {
        $('#val_camp_msg').text('Para enviar un mensaje, los campos nombre y correo no pueden estar vacíos');
        $('#val_camp_msg').css('color', 'red');
        console.log('nombre y correo vasios');
        setTimeout(() => {
            $('#val_camp_msg').text('');
        }, 3000);
    }
    else if (nombre === '') {
        $('#val_nom_contac').text('El campo nombre no puede estar vacío');
        $('#val_nom_contac').css('color', 'red');
        console.log('El campo nombre no puede estar vacío');
        setTimeout(() => {
            $('#val_nom_contac').text('');
        }, 3000);
    }
    else if (email === '') {
        $('#val_email_contac').text('El campo correo no puede estar vacío');
        $('#val_email_contac').css('color', 'red');
        console.log('El campo correo no puede estar vacío');
        setTimeout(() => {
            $('#val_email_contac').text('');
        }, 3000);
    }
    else if (mensaje === '') {
        $('#val_mensaje_contac').text('El campo mensaje no puede estar vacío');
        $('#val_mensaje_contac').css('color', 'red');
        console.log('El campo mensaje no puede estar vacío');
        setTimeout(() => {
            $('#val_mensaje_contac').text('');
        }, 3000);
    }
    else {
        $('#val_nom_contac').text('');
        $('#val_email_contac').text('');
        $('#val_mensaje_contac').text('');
        console.log('Mensaje enviado');
        $('#val_camp_msg').text('Mensaje enviado');
        $('#val_camp_msg').css('color', 'green');
        setTimeout(() => {
            $('#val_camp_msg').text('');
        }, 3000);
    }
}