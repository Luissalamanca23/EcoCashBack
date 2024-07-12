from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Newsletter, Usuario, Rol, Region, Comuna
from .forms import EventoForm, UsuarioForm, NewsletterForm, RegionForm, ComunaForm
from .decorators import role_required
from django.views.decorators.csrf import csrf_exempt


@role_required('Administrador')
def agregar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_evento')
    else:
        form = EventoForm()
    return render(request, 'administracion/eventos/agregar_evento.html', {'form': form})


@role_required('Administrador')
def listar_evento(request):
    eventos = Evento.objects.all()
    return render(request, 'administracion/eventos/listar_eventos.html', {'eventos': eventos})


@role_required('Administrador')
def agregar_suscripcion(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html', {'eventos': Evento.objects.all(), 'message': 'Suscripción exitosa'})
        else:
            return render(request, 'inicio.html', {'eventos': Evento.objects.all(), 'message': 'Por favor, ingresa un email válido.'})
    return redirect('listar_evento')

@role_required('Administrador')
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

@role_required('Administrador')
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'administracion/eventos/eliminar_evento.html', {'evento': evento})

@role_required('Administrador')
def admin_dashboard(request):
    request.session['admin'] = True
    request.session['usuario'] = 'admin'
    usuario = request.session['usuario']
    return render(request, 'administracion/admin.html')

@role_required('Administrador')
def listar_newsletter(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'administracion/newsletter/listar_news.html', {'newsletters': newsletters})

@role_required('Administrador')
def eliminar_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
    if request.method == 'POST':
        newsletter.delete()
        return redirect('listar_newsletter')
    return render(request, 'administracion/newsletter/eliminar_news.html', {'newsletter': newsletter})

@role_required('Administrador')
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
    usuarios = Usuario.objects.all()
    return render(request, 'administracion/users/listar_users.html', {'usuarios': usuarios})

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
            # Asignar rol de usuario por defecto si no se selecciona otro
            if not usuario.rol:
                usuario.rol = Rol.objects.get(nombre='usuario')  # Asegúrate de que el rol 'usuario' existe
            usuario.save()
            return redirect('listar_users')
    else:
        form = UsuarioForm()
    return render(request, 'administracion/users/agregar_user.html', {'form': form})

@role_required('Administrador')
def eliminar_users(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_users')
    return render(request, 'administracion/users/eliminar_user.html', {'usuario': usuario})

@role_required('Administrador')
def region_list(request):
    regiones = Region.objects.all()
    return render(request, 'administracion/ubicacion/region_list.html', {'regiones': regiones})

@role_required('Administrador')
def region_create(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('region_list')
    else:
        form = RegionForm()
    return render(request, 'administracion/ubicacion/region_form.html', {'form': form})

@role_required('Administrador')
def region_update(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect('region_list')
    else:
        form = RegionForm(instance=region)
    return render(request, 'administracion/ubicacion/region_form.html', {'form': form})

@role_required('Administrador')
def region_delete(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        region.delete()
        return redirect('region_list')
    return render(request, 'administracion/ubicacion/region_confirm_delete.html', {'object': region})

@role_required('Administrador')
def comuna_list(request):
    comunas = Comuna.objects.all()
    return render(request, 'administracion/ubicacion/comuna_list.html', {'comunas': comunas})

@role_required('Administrador')
def comuna_create(request):
    if request.method == "POST":
        form = ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comuna_list')
    else:
        form = ComunaForm()
    return render(request, 'administracion/ubicacion/comuna_form.html', {'form': form})

@role_required('Administrador')
def comuna_update(request, pk):
    comuna = get_object_or_404(Comuna, pk=pk)
    if request.method == "POST":
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            form.save()
            return redirect('comuna_list')
    else:
        form = ComunaForm(instance=comuna)
    return render(request, 'administracion/ubicacion/comuna_form.html', {'form': form})

@role_required('Administrador')
def comuna_delete(request, pk):
    comuna = get_object_or_404(Comuna, pk=pk)
    if request.method == "POST":
        comuna.delete()
        return redirect('comuna_list')
    return render(request, 'administracion/ubicacion/comuna_confirm_delete.html', {'object': comuna})