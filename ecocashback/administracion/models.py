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