## Requisitos
- Python 3.12
- Django 5.0.6
- Otros requisitos especificados en `requirements.txt`

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone https://github.com/Luissalamanca23/EcoCashBack.git
    cd ecocashback
    ```

2. Crear y activar un entorno virtual:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Instalar los requisitos:
    ```bash
    pip install -r requirements.txt
    ```

4. Realizar las migraciones:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crear un superusuario para acceder al panel de administración:
    ```bash
    python manage.py createsuperuser
    ```

6. Ejecutar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso
- Acceder a la página de inicio en `http://127.0.0.1:8000/`
- Registrarse como un nuevo usuario en `http://127.0.0.1:8000/accounts/registro/`
- Iniciar sesión en `http://127.0.0.1:8000/accounts/login/`
- Acceder al panel de administración en `http://127.0.0.1:8000/admin/` con el superusuario creado.
- 
- Crear usuario administrador en `http://127.0.0.1:8000/administracion/agregar_user/` ( Para poder tener acceso a el panel administrador, que solo se podra ingresar si eres rol administrador y no usuario)

- La vista crear_user es la unica que no tiene (@role_required('Administrador')), debida a que se necesita poder crear un usuario administrador