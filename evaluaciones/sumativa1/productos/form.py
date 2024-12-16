from django import forms
from django.contrib.auth.models import User
from .models import Producto

class AgregarProductos(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ["nombre", "precio", "marca", "categoria"]
        labels = {
            "nombre":"Nombre del producto",
            "precio":"Precio",
            "marca":"Marca",
            "categoria":"Categoria"
            }

