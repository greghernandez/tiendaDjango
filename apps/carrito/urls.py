from django.urls import path
from apps.carrito.views import carrito, comprar

app_name = 'Carrito'
urlpatterns = [
    path('', carrito, name =  'carrito'),
    path('comprar/<idUsuario>', comprar, name="eliminarRegistro"),
    ]