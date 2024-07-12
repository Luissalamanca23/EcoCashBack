# public/urls.py
from django.urls import path
from . import views
from administracion import views as admin_views

urlpatterns = [
    path('', views.index, name='index'),
    path('suscribirse/', views.agregar_suscripcion, name='agregar_suscripcion'),
    path('admin_dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('agregar_suscripcion/', views.agregar_suscripcion, name='agregar_suscripcion'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('perfil/', views.perfil, name='perfil'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
]