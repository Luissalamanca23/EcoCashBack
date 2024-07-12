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
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contraseña', 'rol']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    def clean_confirmar_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        confirmar_contraseña = self.cleaned_data.get('confirmar_contraseña')
        if contraseña and confirmar_contraseña and contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return confirmar_contraseña

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['contraseña'])
        if commit:
            usuario.save()
        return usuario

class LoginForm(forms.Form):
    email = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)