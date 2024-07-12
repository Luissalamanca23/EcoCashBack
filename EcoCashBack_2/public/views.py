from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from administracion.models import Newsletter
from administracion.models import Evento
from administracion.models import Usuario
from administracion.models import Rol
from administracion.models import Newsletter, Evento
from administracion.forms import NewsletterForm
from .forms import RegistroForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewsletterForm
from .forms import LoginForm
from .forms import EventoForm
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    eventos = Evento.objects.order_by('-fecha')[:2]
    return render(request, 'inicio.html', {'eventos': eventos})


def nosotros(request):
    return render(request, 'sobre-nosotros.html')



@csrf_exempt
def agregar_suscripcion(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html', {'eventos': Evento.objects.all(), 'message': 'Suscripción exitosa'})
        else:
            return render(request, 'inicio.html', {'eventos': Evento.objects.all(), 'message': 'Por favor, ingresa un email válido.'})
    return redirect('listar_evento')




def admin_dashboard(request):
    return render(request, 'administrarador/admin.html')


@login_required
def perfil(request):
    return render(request, 'perfil.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('index')

def contacto(request):
    return render(request, 'contactanos.html')

def servicios(request):
    return render(request, 'servicios.html')

