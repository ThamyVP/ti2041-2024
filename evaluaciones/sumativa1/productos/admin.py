from django.contrib import admin
from .models import Producto, Caracteristicas, Categoria, Marca

# Register your models here.
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Caracteristicas)
admin.site.register(Categoria)
