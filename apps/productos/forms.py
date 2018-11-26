from django import forms
from apps.productos.models import Producto, Categoria

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = [
			'nombre',
			'codigo',
			'caracteristicas',
			'precio',
			'fechaDeRegistro',
			'cantidad',
		]

		labels = {
			'nombre' : 'Nombre',
			'codigo' : 'Código',
			'caracteristicas' : 'Características',
			'precio' : 'Precio',
			'fechaDeRegistro' : 'Fecha de registro',
			'cantidad' : 'Cantidad',
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
			'codigo' : forms.TextInput(attrs={'class': 'form-control'}),
			'caracteristicas' : forms.TextInput(attrs={'class': 'form-control'}),
			'precio' : forms.TextInput(attrs={'class': 'form-control'}),
			'fechaDeRegistro': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
		}
#Formulario Categorías
class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = [
			'nombre',
			'descripcion',
			'fechaDeRegistro',
		]

		labels = {
			'nombre' : 'Nombre',
			'descripcion' : 'Descripción de la categoría',
			'fechaDeRegistro' : 'Fecha de registro',
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion' :forms.TextInput(attrs={'class': 'form-control'}),
			'fechaDeRegistro': forms.TextInput(attrs={'class': 'form-control'}),
		}

class ProductoCarritoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = [
			'nombre',
			'codigo',
			'caracteristicas',
			'precio',
			'fechaDeRegistro'
		]

		labels = {
			'nombre' : 'Nombre',
			'codigo' : 'Código',
			'caracteristicas' : 'Características',
			'precio' : 'Precio',
			'fechaDeRegistro' : 'Fecha de registro'
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'readonly': '', 'class': 'form-control'}),
			'codigo' : forms.TextInput(attrs={'readonly': '', 'class': 'form-control'}),
			'caracteristicas' : forms.TextInput(attrs={'readonly': '', 'class': 'form-control'}),
			'precio' : forms.TextInput(attrs={'readonly': '', 'class': 'form-control'}),
			'fechaDeRegistro': forms.TextInput(attrs={'readonly': '', 'class': 'form-control'})
		}
			
