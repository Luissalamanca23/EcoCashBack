from django.urls import path
from . import views
from .views import (
    region_list, region_create, region_update, region_delete,
    comuna_list, comuna_create, comuna_update, comuna_delete,
    listar_users, modificar_users, eliminar_users, agregar_usuario
)
from public.views import index, agregar_suscripcion, contacto, servicios

urlpatterns = [
    path('agregar_evento/', views.agregar_evento, name='agregar_evento'),
    path('eliminar_evento/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),
    path('listar_evento/', views.listar_evento, name='listar_evento'),
    path('modificar_evento/<int:pk>/', views.modificar_evento, name='modificar_evento'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('listar_newsletter/', views.listar_newsletter, name='listar_newsletter'),
    path('eliminar_newsletter/<int:pk>/', views.eliminar_newsletter, name='eliminar_newsletter'),
    path('modificar_newsletter/<int:pk>/', views.modificar_newsletter, name='modificar_newsletter'),

    path('listar_users/', views.listar_users, name='listar_users'),
    path('agregar_user/', views.agregar_usuario, name='agregar_usuario'),   
    path('modificar_user/<int:pk>/', views.modificar_users, name='modificar_users'),
    path('eliminar_user/<int:pk>/', views.eliminar_users, name='eliminar_users'),

    path('regiones/', region_list, name='region_list'),
    path('regiones/nueva/', region_create, name='region_create'),
    path('regiones/<int:pk>/editar/', region_update, name='region_update'),
    path('regiones/<int:pk>/eliminar/', region_delete, name='region_delete'),
    
    path('comunas/', comuna_list, name='comuna_list'),
    path('comunas/nueva/', comuna_create, name='comuna_create'),
    path('comunas/<int:pk>/editar/', comuna_update, name='comuna_update'),
    path('comunas/<int:pk>/eliminar/', comuna_delete, name='comuna_delete'),

    path('agregar_suscripcion/', agregar_suscripcion, name='agregar_suscripcion'),
]
