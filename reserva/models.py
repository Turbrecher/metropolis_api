from django.db import models
from cartelera.models import Pelicula
from autenticacion.models import Usuario

# Aqui iran los modelos relacionados con la reserva de entradas de sesiones.

#Sala de cine.
class Sala(models.Model):
    nombre = models.TextField()
    aforo = models.IntegerField()
    
#Sesion en una sala de una pelicula.
class Sesion(models.Model):
    id_pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    
#Entrada de una sesion de cine.
class Entrada(models.Model):
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_sesion = models.ForeignKey(Sesion,on_delete=models.CASCADE)
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField()
    
    
