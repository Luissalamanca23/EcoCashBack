from django.urls import path
from . import views

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
]
