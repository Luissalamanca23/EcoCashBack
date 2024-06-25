from django import forms
from .models import Newsletter
from .models import Evento



class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email', 'tipo_suscripcion']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'ubicacion', 'comuna']

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')