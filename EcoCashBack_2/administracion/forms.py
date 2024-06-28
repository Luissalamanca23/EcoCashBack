from django import forms
from .models import Evento
from .models import Usuario
from .models import Region, Comuna
from .models import Newsletter

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email', 'usuario', 'tipo_suscripcion']

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nombre']

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['nombre', 'region']


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'ubicacion', 'comuna']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'contraseña', 'rol']

class LoginForm(forms.Form):
    email = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)