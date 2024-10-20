from django.db import models


# Create your models here.

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Caracteristicas(models.Model):
    id_caracteristica = models.AutoField(primary_key=True)
    tamano = models.IntegerField()
    peso = models.IntegerField()

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, null=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre +' '+ str(self.marca) 