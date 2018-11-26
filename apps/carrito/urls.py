from django.urls import path
from apps.carrito.views import carrito

app_name = 'carrito'
urlpatterns = [
    path('', carrito, name =  'carrito')
    ]