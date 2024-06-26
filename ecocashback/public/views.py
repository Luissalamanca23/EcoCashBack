from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from administracion.models import Newsletter
from administracion.models import Evento
from administracion.models import Usuario

from .forms import NewsletterForm
from .forms import LoginForm
from .forms import EventoForm
from django.contrib import messages
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    eventos = Evento.objects.all()
    return render(request, 'inicio.html', {'eventos': eventos})


@ensure_csrf_cookie
def debug_csrf_view(request):
    if request.method == 'POST':
        return HttpResponse("CSRF token received.")
    return HttpResponse("CSRF token set.")





# eventos ecocashback 

def mostrar(request):
    # Ordena los eventos por fecha de manera descendente y toma los últimos 2
    eventos = Evento.objects.order_by('-fecha')[:2]
    return render(request, 'public/inicio.html', {'eventos': eventos})
@csrf_exempt
def agregar_suscripcion(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html', {'eventos': Evento.objects.all(), 'message': 'Suscripción exitosa'})
        else:
            return render(request, 'inicio.html', {'eventos': Evento.objects.all(), 'message': 'Por favor, ingresa un email válido.'})
    return redirect('listar_eventos')

def login_view(request):
    if request.method == 'POST':
        print("POST request received")
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            if user.rol.nombre == 'Administrador':
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            return HttpResponse("Invalid login details")
    else:
        print("Rendering login page")
        return render(request, 'login.html')

def verificar_usuario(request):
    if request.user.is_authenticated:
        usuario_val = Usuario.objects.get(email=request.user.email)
        if usuario_val.rol.nombre == 'Administrador':
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    else:
        return redirect('login_view')



def user_dashboard(request):
    return render(request, 'user.html')

def admin_dashboard(request):
    return render(request, 'administrarador/admin.html')


def create_user(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_users')
    else:
        form = UsuarioForm()
    return render(request, 'public/users/agregar_user.html', {'form': form})