from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from .models import Newsletter
from .models import Usuario 
from .models import Rol
from .forms import EventoForm, UsuarioForm

def agregar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_evento')
    else:
        form = EventoForm()
    return render(request, 'administracion/eventos/agregar_evento.html', {'form': form})

def listar_evento(request):
    eventos = Evento.objects.all()
    return render(request, 'administracion/eventos/listar_eventos.html', {'eventos': eventos})



def modificar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_evento')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'administracion/eventos/modificar_evento.html', {'form': form})

def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'administracion/eventos/eliminar_evento.html', {'evento': evento})


def admin_dashboard(request):
    return render(request, 'administracion/admin.html')


def listar_newsletter(request):
    newsletter = Newsletter.objects.all()
    return render(request, 'administracion/newsletter/listar_news.html', {'newsletter': newsletter})

def eliminar_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
    if request.method == 'POST':
        newsletter.delete()
        return redirect('listar_newsletter')
    return render(request, 'administracion/newsletter/eliminar_news.html', {'newsletter': newsletter})

def modificar_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, instance=newsletter)
        if form.is_valid():
            form.save()
            return redirect('listar_newsletter')
    else:
        form = NewsletterForm(instance=newsletter)
    return render(request, 'administracion/newsletter/modificar_news.html', {'form': form})

def listar_users(request):
    usuario = Usuario.objects.all()
    return render(request, 'administracion/users/listar_users.html', {'usuario': usuario})

def modificar_users(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_users')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'administracion/users/modificar_user.html', {'form': form})


def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['contraseña'])
            usuario.save()
            return redirect('listar_users')
    else:
        form = UsuarioForm()
    return render(request, 'administracion/users/agregar_user.html', {'form': form})

def eliminar_users(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_users')
    return render(request, 'administracion/users/eliminar_user.html', {'usuario': usuario})