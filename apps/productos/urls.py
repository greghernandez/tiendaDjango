"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from apps.productos.views import ViewProducto,categorias,nuevoRegistro, editarRegistro, eliminarRegistro, nuevoRegistroCat, editarRegistroCat, eliminarRegistroCat, agregarCarrito

app_name = 'Productos'
urlpatterns = [
    path('listado', ViewProducto.as_view() , name =  'listado'),
    path('categorias', categorias , name =  'categorias'),

    #URLS Productos
    path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
    path('editarRegistro/<idProducto>', editarRegistro, name="editarRegistro"),
    path('eliminarRegistro/<idProducto>', eliminarRegistro, name="eliminarRegistro"),
    #URLS Categorias
    path('nuevoRegistroCat', nuevoRegistroCat, name="nuevoRegistroCat"),
    path('editarRegistrocat/<idCategoria>', editarRegistroCat, name="editarRegistroCat"),
    path('eliminarRegistrocat/<idCategoria>', eliminarRegistroCat, name="eliminarRegistroCat"),
    #agregarCarrito
    path('agregarCarrito/<idProducto>', agregarCarrito, name="agregarCarrito")
]
