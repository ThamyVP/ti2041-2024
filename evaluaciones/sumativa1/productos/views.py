from django.shortcuts import render, redirect
from .models import Producto, Marca,Caracteristicas, Categoria

def index(request):
    all_productos = Producto.objects.all().order_by('codigo')
    
    productos_actuales = []
    for producto in all_productos:
        producto_actual = {
            'codigo': producto.codigo,
            'nombre': producto.nombre,
            'precio' : producto.precio,
            'marca' : producto.marca,
            'categoria' : producto.categoria,
        }
        productos_actuales.append(producto_actual)
    
    context = { 'productos': productos_actuales }
    return render(request, 'index.html', context)
    


def registro(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        marca_id = request.POST.get('marca_id')
        categoria_id = request.POST.get('categoria_id')

        marca = Marca.objects.get(id_marca = marca_id) 
        categoria = Categoria.objects.get(id_categoria = categoria_id) 

        producto = Producto (
            codigo = codigo,
            nombre = nombre,
            precio = precio,
            marca = marca,
            categoria = categoria
        )
        producto.save()

        return redirect(index)
    else:
        return render (request,'registro.html')