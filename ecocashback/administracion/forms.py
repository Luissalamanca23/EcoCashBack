from django import forms
from .models import Evento
from .models import Usuario
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email', 'tipo_suscripcion']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'ubicacion', 'comuna']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'rol'] 

from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)