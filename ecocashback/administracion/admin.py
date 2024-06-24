from django.contrib import admin
from .models import (Comuna, Evento, Region, Newsletter, Usuario, Rol)
# Register your models here.
admin.site.register(Comuna)
admin.site.register(Evento)
admin.site.register(Region)
admin.site.register(Newsletter)
admin.site.register(Usuario)
admin.site.register(Rol)