from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm

def agregar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')  # Asegúrate de que 'listar_eventos' esté definido en tus URLs
    else:
        form = EventoForm()
    return render(request, 'administracion/agregar_evento.html', {'form': form})
