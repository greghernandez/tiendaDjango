from django.db import models

# Create your models here.
class Carrito(models.Model):
	usuario = models.CharField(max_length=30)
	producto = models.IntegerField(default = 0)
	cantidad = models.IntegerField(default = 0)
	nombreProducto = models.CharField(max_length=30, default = 'Sin Nombre')
	precio = models.IntegerField(default = 0)