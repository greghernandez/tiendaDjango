from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic  import ListView
from apps.carrito.models import Carrito

# Create your views here.

def carrito(request):
	contexto = { 
		'carrito': Carrito.objects.all()
	}
	return render(request, 'carrito/index.html', contexto)

def comprar(request, idUsuario):
	listaCompra = Carrito.objects.get(usuario = idUsuario)
	listaCompra.delete()
	return redirect('Productos:listado');

