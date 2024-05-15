from django.db import models
#En este archivo modelo iran los datos relacionados con la cartelera de cine.

#Calificacion por edades
class Pegi(models.Model):
    nombre = models.TextField()
    
#Genero de pelicula
class Genero(models.Model):
    nombre = models.TextField()
    
#Actor de una pelicula
class Actor(models.Model):
    nombre = models.TextField()
    link_imdb = models.TextField()

#Pelicula de la cartelera
class Pelicula(models.Model):
    url_trailer = models.TextField()
    cartel = models.ImageField()
    fecha_lanzamiento = models.DateField()
    director = models.TextField()
    titulo = models.TextField()
    duracion = models.FloatField()
    sinopsis = models.TextField()
    id_pegi = models.ForeignKey(Pegi, on_delete=models.CASCADE)
    
#Generos de una pelicula (es una tabla adicional porque una pelicula puede
# tener varios generos y un genero puede estar en varias peliculas)
class PeliculaGenero(models.Model):
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
#Actuaciones de un actor (es una tabla adicional porque un actor
# puede actuar en varias peliculas y una pelicula tener varios actores)
class Interpretacion(models.Model):
    id_actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
    id_pelicula = models.ForeignKey(Pelicula,on_delete=models.CASCADE)

    
