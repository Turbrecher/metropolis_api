from django.db import models
from cartelera.models import Pelicula
from django.contrib.auth.models import User

# Aqui iran los modelos relacionados con la reserva de entradas de sesiones de cine.

#Sala de cine.
class Sala(models.Model):
    nombre = models.TextField()
    aforo = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
#Sesion en una sala de una pelicula.
class Sesion(models.Model):
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, related_name="sala",on_delete=models.CASCADE)
    hora = models.TimeField()
    
    def __str__(self):
        return  self.pelicula.__str__() + " // " + str(self.hora.hour) + " : " +  str(self.hora.minute)
    
#Entrada de una sesion de cine.
class Entrada(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    sesion = models.ForeignKey(Sesion,on_delete=models.CASCADE)
    nombre = models.TextField()
    fecha_compra = models.DateField()
    descripcion = models.TextField()
    precio = models.FloatField()
    
    def __str__(self):
        return self.nombre
    
    
