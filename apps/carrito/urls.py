from django.urls import path
from apps.carrito.views import carrito

app_name = 'Carrito'
urlpatterns = [
    path('', carrito, name =  'carrito')
    ]