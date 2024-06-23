# public/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.listar_eventos, name='listar_eventos'),
    path('suscribirse/', views.agregar_suscripcion, name='agregar_suscripcion'),
]
