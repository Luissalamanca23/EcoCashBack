from django.urls import path
from . import views

urlpatterns = [
    path('agregar_evento/', views.agregar_evento, name='agregar_evento'),
]
