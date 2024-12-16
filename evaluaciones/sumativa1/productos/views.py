from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca, Caracteristicas, Categoria
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import logout
from django.utils.timezone import now
from .form import AgregarProductos
from .utils import generar_token



@login_required
def index(request):
    all_productos = Producto.objects.all().order_by('codigo')
    token = request.session.get('token', '')
    context = {
        'productos': all_productos,
        'token': token 
        }
    return render(request, 'index.html', context)

@login_required
def registro(request):
    if request.method == 'POST':
        formulario = AgregarProductos(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = AgregarProductos()
    return render (request, 'registro.html', {"formulario": formulario})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Iniciar sesión
            login(request, user)

            #variables de sesión
            token = generar_token(user)
            request.session['token'] = token

            request.session['username'] = user.username
            request.session['login_date'] = now().strftime('%Y-%m-%d %H:%M:%S')  # Formato legible
            request.session['grupo'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()

            return redirect('lista_productos')
        else:
            messages.error(request, 'Usuario o clave incorrectos')

    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    logout(request)
    return redirect('/')

def grupo(user):
    return user.groups.filter(name='grupo').exists()

def editar(request, codigo):
    producto= get_object_or_404(Producto, codigo = codigo)
    if request.method == 'POST':
        formulario = AgregarProductos(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = AgregarProductos(instance=producto)
    return render(request, 'editar.html', {'formulario': formulario})
        