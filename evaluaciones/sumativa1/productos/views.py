from django.shortcuts import render, redirect

productos_registrados = []

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        marca = request.POST.get('marca')
        fecha = request.POST.get('fecha')

        # Crear un diccionario que represente el producto y añadirlo a la lista
        producto = {
            'nombre': nombre,
            'codigo': codigo,
            'marca': marca,
            'fecha': fecha,
        }
        productos_registrados.append(producto)

        # Redirigir a la lista de productos después de registrar uno
        return redirect('consulta')

    return render(request, 'registro.html')

def consulta(request):
    # Pasar la lista de productos registrados a la plantilla
    return render(request, 'consulta.html', {'productos': productos_registrados})