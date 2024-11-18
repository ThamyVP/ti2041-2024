from django.shortcuts import render, redirect
from .models import Producto, Marca,Caracteristicas, Categoria
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import logout
from django.utils.timezone import now


@login_required
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

@login_required
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

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Iniciar sesión
            login(request, user)

            #variables de sesión
            request.session['username'] = user.username
            request.session['login_date'] = now().strftime('%Y-%m-%d %H:%M:%S')  # Formato legible
            request.session['grupo'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()

            return redirect('lista_productos')
        else:
            messages.error(request, 'Usuario o clave incorrectos')

    return render(request, 'login.html')

@login_required
def lista_productos(request):
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
    
    return render(request, 'productos/consulta.html', {'productos': productos_actuales})

def logout_view(request):
    request.session.flush()
    logout(request)
    return redirect('/')

def grupo(user):
    return user.groups.filter(name='grupo').exists()