from django.db import models
from cartelera.models import Pelicula
from compra.models import TipoEntrada
from django.contrib.auth.models import User

# Aqui iran los modelos relacionados con la reserva de entradas de sesiones de cine.

class Sillon(models.Model):
    fila = models.IntegerField()
    columna = models.IntegerField()

#Sala de cine.
class Sala(models.Model):
    nombre = models.TextField()
    aforo = models.IntegerField()
    sillones = models.ManyToManyField(Sillon)
    
    def __str__(self):
        return self.nombre
    
#Sesion en una sala de una pelicula.
class Sesion(models.Model):
    pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, related_name="sala",on_delete=models.CASCADE)
    hora = models.TimeField()
    sillones_ocupados = models.ManyToManyField(Sillon)
    
    class Meta:
        unique_together = ('sala', 'hora',)
    
    def __str__(self):
        return  self.pelicula.__str__() + " // " + str(self.hora.hour) + " : " +  str(self.hora.minute)
    
#Entrada de una sesion de cine.
class Entrada(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    sesion = models.ForeignKey(Sesion,on_delete=models.CASCADE)
    #sillon = models.ForeignKey(Sillon, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
    tipo_entrada = models.ForeignKey(TipoEntrada, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    

    
    
