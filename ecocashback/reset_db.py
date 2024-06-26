# reset_db.py

import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecocashback.settings')
django.setup()

# Eliminar la base de datos y las migraciones
os.system('rm -rf ecocashback/administracion/migrations')
os.system('rm -rf ecocashback/public/migrations')
os.system('rm -f db.sqlite3')

# Ejecutar la eliminación de tablas directamente
with connection.cursor() as cursor:
    cursor.execute("DROP TABLE IF EXISTS administracion_rolpermiso;")
    cursor.execute("DROP TABLE IF EXISTS administracion_newsletter;")
    cursor.execute("DROP TABLE IF EXISTS administracion_usuario;")
    cursor.execute("DROP TABLE IF EXISTS administracion_rol;")
    cursor.execute("DROP TABLE IF EXISTS administracion_permiso;")

# Crear nuevas migraciones y aplicar
os.system('python3 manage.py makemigrations administracion')
os.system('python3 manage.py makemigrations public')
os.system('python3 manage.py migrate')
