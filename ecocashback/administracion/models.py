from django.db import models

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

class Evento(models.Model):
    evento_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Newsletter(models.Model):
    newsletter_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    tipo_suscripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre