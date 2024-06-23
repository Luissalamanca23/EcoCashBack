document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-suscripcion');
    const emailInput = document.getElementById('email-suscripcion');
    const messageContainer = document.getElementById('mensaje');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const email = emailInput.value.trim();
        const tipo_suscripcion = form.querySelector('select[name="tipo_suscripcion"]').value;
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        // Validar que el email no esté vacío
        if (!email) {
            showMessage('El email es obligatorio.', 'error');
            return;
        }

        // Validar el formato del email
        if (!isValidEmail(email)) {
            showMessage('El formato del email es incorrecto.', 'error');
            return;
        }

        // Enviar la solicitud AJAX para verificar y guardar el email
        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ email: email, tipo_suscripcion: tipo_suscripcion })
        })
        .then(response => response.json())
        .then(data => {
            showMessage(data.message, data.status);
        })
        .catch(error => {
            showMessage('Ocurrió un error. Por favor, inténtalo de nuevo.', 'error');
        });
    });

    function isValidEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    function showMessage(message, type) {
        messageContainer.innerText = message;
        messageContainer.className = 'msg ' + type;
        messageContainer.style.display = 'block';
    }
});
