from django.contrib.auth.backends import BaseBackend
from administracion.models import Usuario

class CustomBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        print(f"Authenticating user with email: {email}")
        try:
            user = Usuario.objects.get(email=email)
            print(f"Checking password for user {email}")
            if user.check_password(password):
                print("Password check successful")
                return user
            else:
                print("Password check failed")
                return None
        except Usuario.DoesNotExist:
            print(f"User with email {email} does not exist")
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
