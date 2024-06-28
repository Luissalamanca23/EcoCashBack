from django.contrib import admin
from .models import Usuario, Newsletter, Evento, Comuna, Region, Rol

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Newsletter)
admin.site.register(Evento)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Rol)