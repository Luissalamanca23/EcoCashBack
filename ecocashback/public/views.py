from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Newsletter
from administracion.models import Evento
from .forms import NewsletterForm
import json
from django.shortcuts import render

def index(request):
    eventos = Evento.objects.all()
    return render(request, 'inicio.html', {'eventos': eventos})








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
            return render(request, 'public/inicio.html', {'eventos': Evento.objects.all(), 'message': 'Suscripción exitosa'})
        else:
            return render(request, 'public/inicio.html', {'eventos': Evento.objects.all(), 'message': 'Por favor, ingresa un email válido.'})
    return redirect('listar_eventos')