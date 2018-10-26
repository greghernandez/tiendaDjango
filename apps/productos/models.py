from django.db import models

# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=30)
	codigo = models.IntegerField(default = 0)
	caracteristicas = models.CharField(max_length = 150, default = ' - Sin caracteristicas -')
	precio = models.IntegerField(default = 0)
	fechaDeRegistro = models.DateField(default = '2000-01-01')
	cantidad = models.IntegerField(default = 0)

class Categoria(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length = 150, default = 'Sin descripción')
	fechaDeRegistro = models.DateField(default = '2000-01-01')