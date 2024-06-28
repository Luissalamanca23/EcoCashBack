# public/urls.py
from django.urls import path
from . import views
from administracion import views as admin_views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.mostrar, name='mostrar'),
    path('suscribirse/', views.agregar_suscripcion, name='agregar_suscripcion'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('verificar_usuario/', views.verificar_usuario, name='verificar_usuario'),
    path('agregar_suscripcion/', views.agregar_suscripcion, name='agregar_suscripcion'),
    path('register/', views.create_user, name='register'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
]