from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic  import ListView
from apps.productos.models import Producto, Categoria
from apps.carrito.models import Carrito
from apps.productos.forms import ProductoForm, CategoriaForm, ProductoCarritoForm
import MySQLdb

# Create your views here.

def listado(request):
	contexto = { 
		'productos': Producto.objects.all()
	}
	return render(request, 'productos/listado.html', contexto)

def categorias(request):
	contexto = { 
		'categorias': Categoria.objects.all()
	}
	return render(request, 'categorias/index.html', contexto)

class ViewProducto(ListView):
	model =  Producto
	template_name = 'productos/listado.html'


def nuevoRegistro(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('Productos:listado');
	else:
		form = ProductoForm()
	return render(request, 'productos/ProductosFormulario.html', {'form' : form}) 
		

	form = ProductoForm()
	return render(request, 'productos/ProductosFormulario.html', {'form' : form})

def editarRegistro(request, idProducto):
	producto = Producto.objects.get(id = idProducto)
	if (request.method == 'GET'):
		form = ProductoForm(instance=producto)
	else:
		form = ProductoForm(request.POST, instance = producto)
		if form.is_valid():
			form.save();
		return redirect('Productos:listado')
	return render(request, 'productos/ProductosFormulario.html', {'form' : form})

def eliminarRegistro(request, idProducto):
	producto = Producto.objects.get(id = idProducto)
	producto.delete()
	return redirect('Productos:listado');

##
## -- Views Categorias
##

def nuevoRegistroCat(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('Productos:categorias');
	else:
		form = CategoriaForm()
	return render(request, 'categorias/categoriasFormulario.html', {'form' : form}) 
		

	form = CategoriaForm()
	return render(request, 'productos/ProductosFormulario.html', {'form' : form})

def editarRegistroCat(request, idCategoria):
	categoria = Categoria.objects.get(id = idCategoria)
	if (request.method == 'GET'):
		form = CategoriaForm(instance=categoria)
	else:
		form = CategoriaForm(request.POST, instance = categoria)
		if form.is_valid():
			form.save();
		return redirect('Productos:categorias')
	return render(request, 'categorias/categoriasFormulario.html', {'form' : form})

def eliminarRegistroCat(request, idCategoria):
	categoria = Categoria.objects.get(id = idCategoria)
	categoria.delete()
	return redirect('Productos:categorias');


def agregarCarrito(request, idProducto):
	prod = Producto.objects.get(id = idProducto)
	user = request.user.id

	a = Carrito(producto=idProducto, usuario= user, nombreProducto= prod.nombre ,cantidad = '1', precio = prod.precio)
	a.save()
	return redirect('/');
	