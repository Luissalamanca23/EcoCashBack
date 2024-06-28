from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100) 
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Facturacion(models.Model):
    factura_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.SET_NULL, null=True)
    fecha_emision = models.DateTimeField()
    monto_total = models.IntegerField()

    def __str__(self):
        return f'Factura {self.factura_id}'

class Suscripcion(models.Model):
    suscripcion_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    tipo_suscripcion = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return self.tipo_suscripcion

class Residuo(models.Model):
    residuo_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    tipo_residuo = models.CharField(max_length=50)
    peso = models.IntegerField()
    precio = models.IntegerField()
    estado = models.CharField(max_length=50)
    fecha_recoleccion = models.DateTimeField()
    puntos_calculados = models.IntegerField()

    def __str__(self):
        return self.tipo_residuo

class Punto(models.Model):
    puntos_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return str(self.puntos)

class Recompensa(models.Model):
    recompensa_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    puntos_necesarios = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Transaccion(models.Model):
    transaccion_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    recompensa = models.ForeignKey('Recompensa', on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    puntos_usados = models.IntegerField()

    def __str__(self):
        return f'Transacción {self.transaccion_id}'

class Contenedor(models.Model):
    contenedor_id = models.AutoField(primary_key=True)
    tipo_contenedor = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo_contenedor

class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class LogActividad(models.Model):
    log_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    actividad = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.actividad

class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)

    def __str__(self):
        return self.direccion

class Evento(models.Model):
    evento_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    actividad_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    comuna_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Newsletter(models.Model):
    newsletter_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    tipo_suscripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class NotificacionLanzamiento(models.Model):
    notificacion_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.email

class Auditoria(models.Model):
    auditoria_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Auditoria {self.auditoria_id}'

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100)
    cantidad_disponible = models.IntegerField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.producto

class TotalCantidadResiduos(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    tipo_residuo = models.CharField(max_length=50)
    cantidad_total = models.IntegerField()

    def __str__(self):
        return self.tipo_residuo

class CalculoCO2(models.Model):
    co2_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    cantidad_co2 = models.IntegerField()
    fecha = models.DateTimeField()

    def __str__(self):
        return f'Calculo CO2 {self.co2_id}'
