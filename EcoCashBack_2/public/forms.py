from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Evento
from .models import Newsletter
from  .models import Usuario

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

class RegistroForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contraseña']

    def clean_confirmar_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        confirmar_contraseña = self.cleaned_data.get('confirmar_contraseña')
        if contraseña and confirmar_contraseña and contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return confirmar_contraseña

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.contraseña = self.cleaned_data['contraseña']
        if commit:
            usuario.save()
        return usuario

