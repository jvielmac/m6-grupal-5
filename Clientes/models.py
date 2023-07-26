from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)