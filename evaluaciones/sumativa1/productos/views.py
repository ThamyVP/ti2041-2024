from django.shortcuts import render, redirect
from .models import Post

productos_registrados = []

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        marca = request.POST.get('marca')
        fecha = request.POST.get('fecha')

        producto = {
            'nombre': nombre,
            'codigo': codigo,
            'marca': marca,
            'fecha': fecha,
        }
        productos_registrados.append(producto)

        return redirect('consulta')

    return render(request, 'registro.html')

def consulta(request):

    return render(request, 'consulta.html', {'productos': productos_registrados})

