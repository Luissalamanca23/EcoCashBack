from django.contrib import admin
from .models import Usuario, Newsletter, Evento, Comuna, Region, Rol, Punto, LogActividad, Direccion, Actividad, Residuo, TotalCantidadResiduos, CalculoCO2

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Newsletter)
admin.site.register(Evento)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Rol)
admin.site.register(Punto)
admin.site.register(LogActividad)
admin.site.register(Direccion)
admin.site.register(Actividad)
admin.site.register(Residuo)
admin.site.register(TotalCantidadResiduos)
admin.site.register(CalculoCO2)