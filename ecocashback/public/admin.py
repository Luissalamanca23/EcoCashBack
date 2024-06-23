from django.contrib import admin
from .models import (
    Usuario, Facturacion, Suscripcion, Residuo, Punto, Recompensa,
    Transaccion, Contenedor, Empresa, Empleado, Rol, Permiso,
    RolPermiso, LogActividad, Direccion, Evento, Actividad, Comuna,
    Region, Newsletter, NotificacionLanzamiento, Auditoria, Stock,
    TotalCantidadResiduos, CalculoCO2
)


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Facturacion)
admin.site.register(Suscripcion)
admin.site.register(Residuo)
admin.site.register(Punto)
admin.site.register(Recompensa)
admin.site.register(Transaccion)
admin.site.register(Contenedor)
admin.site.register(Empresa)
admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(Permiso)
admin.site.register(RolPermiso)
admin.site.register(LogActividad)
admin.site.register(Direccion)
admin.site.register(Evento)
admin.site.register(Actividad)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Newsletter)
admin.site.register(NotificacionLanzamiento)
admin.site.register(Auditoria)
admin.site.register(Stock)
admin.site.register(TotalCantidadResiduos)
admin.site.register(CalculoCO2)