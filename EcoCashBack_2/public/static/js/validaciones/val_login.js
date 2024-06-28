var users = 'admin@gmail.com';

var password = admin123;


function validarFormulario(event) {
    event.preventDefault();
    $('.formulario-login').submit(function(event) {
        var email = $('#email_login').val();
        var password = $('#password_email').val();

        if (email !== users || password !== password) {
            event.preventDefault();
            alert('Usuario o contraseña incorrectos');
        }
        else {
            alert('Bienvenido');
        }
    });
}
