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
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))