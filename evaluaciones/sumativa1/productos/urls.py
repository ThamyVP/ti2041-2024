from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),  
    path('productos/', views.index, name='lista_productos'),
    path('productos/registro/', views.registro, name='registro'),  
    path('logout/', views.logout_view, name='logout'),
    path('productos/editar/<int:codigo>/',views.editar, name='editar_producto')
]

    