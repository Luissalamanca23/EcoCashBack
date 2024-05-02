
// validar email y que tenga formato de email


function validar_email(event) {
    event.preventDefault(); // Añade esto
    var email = document.getElementById('email-suscripcion').value;
    var regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    var mensaje = document.getElementById('mensaje');
    if (regex.test(email)) {
        console.log('El correo electrónico es válido');
        mensaje.textContent = 'Te as suscrito correctamente a nuestro boletín';
        mensaje.style.backgroundColor = '#42ac25c0';
    } else {
        console.log('El correo electrónico no es válido');
        mensaje.textContent = 'El correo electrónico no es válido o está vacío ';
        mensaje.style.backgroundColor = '#ff0000';
    }
    mensaje.style.display = 'inline-block';
}