from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.user.username
    
    
class Marca(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    nuevo = models.BooleanField(default=False)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='productos/', blank=True)

    def __str__(self):
        return self.nombre