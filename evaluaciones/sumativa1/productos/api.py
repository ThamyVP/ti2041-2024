from ninja import NinjaAPI, Schema
from django.contrib.auth import authenticate
from django.http import HttpRequest, Http404
from django.shortcuts import get_object_or_404
from pydantic import ValidationError
from .models import Producto, Marca, Categoria
from .utils import generar_token, JWTAuth

# Crea la API
api = NinjaAPI()

# Crea el objeto auth
auth = JWTAuth()

# Manejadores de Errores
@api.exception_handler(Http404)
def error_404(request, ex):
    return api.create_response(request, 
        {'response': 'Recurso no encontrado'},
        status=404)
    
@api.exception_handler(ValidationError)
def error_validacion(request, ex):
    return api.create_response(request,
        {
            'response': 'Error de Formato de Entrada',
            'errores': ex.errors()
        },
        status=422)

# Servicios de la API
class AuthRequest(Schema):
    username: str 
    password: str
    
@api.post(path="/token", tags=["Auth"])
def get_token(request, data: AuthRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        return { "error": "Credenciales inválidas" }
    token = generar_token(user)
    return { "token": token }


@api.get(path="/productos", auth=auth, tags=["Productos"])
def obtener_productos(request):
    lista_productos = Producto.objects.all().values()
    return list(lista_productos)

@api.get(path="/productos/{codigo}", auth=auth, tags=["Productos"])
def obtener_producto(request, codigo: int):
    producto = Producto.objects.filter(codigo = codigo).values()
    return list(producto)

class ProductosSchema(Schema):
    nombre: str
    precio: int
    marca: int
    categoria: int

@api.post(path="/productos", auth=auth, tags=["Productos"])
def agregar_producto(request, data: ProductosSchema):
    marca = Marca.objects.get(pk = data.marca)
    categoria = Categoria.objects.get(pk = data.categoria)
    producto = Producto(
        nombre = data.nombre,
        precio = data.precio,
        marca = marca,
        categoria = categoria
    )
    producto.save()

    return { "mensaje": f"Producto guardado, {producto.nombre}" }

@api.delete(path="/productos/{codigo}", auth=auth, tags=["Productos"])
def eliminar_producto(request, codigo: int):
    producto = Producto.objects.filter(codigo = codigo).first()
    if not producto:
        raise Http404 ('Producto no encontrado')
    producto.delete()
    return { "mensaje": "Producto eliminado" }

@api.put(path="/productos/{codigo}", auth=auth, tags=["Productos"])
def editar_producto(request, codigo: int, data: ProductosSchema):
    producto = get_object_or_404(Producto, codigo = codigo)
    for attr, value in data.dict().items():
        if attr == "marca":
            value = get_object_or_404(Marca, id_marca=value)
        elif attr == "categoria":
            value = get_object_or_404(Categoria, id_categoria=value)
        setattr(producto, attr, value)
    producto.save()
    return { "mensaje": f"Producto actualizado" }

    