from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic  import ListView
from apps.productos.models import Producto, Categoria

# Create your views here.

def index(request):
	contexto = { 
		'categorias': Categoria.objects.all(),
		'productos': Producto.objects.all()
	}
	return render(request, 'index/index.html', contexto)
