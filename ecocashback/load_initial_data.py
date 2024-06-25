import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecocashback.settings")
django.setup()

from administracion.models import Rol, Usuario

def create_roles():
    roles = ["Administrador", "Usuario"]
    for rol in roles:
        obj, created = Rol.objects.get_or_create(nombre=rol)
        if created:
            print(f"Rol '{rol}' creado.")
        else:
            print(f"Rol '{rol}' ya existe.")

def create_admin_user():
    try:
        rol_admin = Rol.objects.get(nombre="Administrador")
        admin_user, created = Usuario.objects.get_or_create(
            email="admin@example.com",
            defaults={
                "nombre": "Admin",
                "rol": rol_admin
            }
        )
        if created:
            admin_user.set_password("admin123")
            admin_user.save()
            print("Usuario administrador creado.")
        else:
            print("Usuario administrador ya existe.")
    except Rol.DoesNotExist:
        print("Rol 'Administrador' no encontrado. Por favor, crea los roles primero.")

if __name__ == "__main__":
    create_roles()
    create_admin_user()
