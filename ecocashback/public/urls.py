# public/urls.py
from django.urls import path
from . import views
from administracion import views as admin_views
from .views import debug_csrf_view
from .views import login_view

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.mostrar, name='mostrar'),
    path('debug-csrf/', debug_csrf_view, name='debug_csrf'),
    path('suscribirse/', views.agregar_suscripcion, name='agregar_suscripcion'),
    path('login/', login_view, name='login'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('verificar_usuario/', views.verificar_usuario, name='verificar_usuario'),
    path('register/', views.create_user, name='register'),
    path('home/', views.home_view, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
]