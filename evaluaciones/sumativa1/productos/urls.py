from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('consulta/', views.consulta, name='consulta'),
    
]