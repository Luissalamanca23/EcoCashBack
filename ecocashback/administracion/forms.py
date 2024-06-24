from django import forms
from .models import Evento
from .models import Usuario

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'ubicacion', 'comuna']




class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contraseña', 'rol']
        widgets = {
            'contraseña': forms.PasswordInput(),  # Para que el campo de contraseña se renderice como un campo de contraseña
        }