from django.db import models
#En este archivo modelo iran los datos relacionados con la cartelera de cine.
    

#Pelicula de la cartelera
class Pelicula(models.Model):
    url_trailer = models.TextField()
    cartel = models.ImageField()
    fecha_lanzamiento = models.DateField()
    director = models.TextField()
    genero = models.TextField()
    pegi = models.TextField()
    titulo = models.TextField()
    duracion = models.FloatField()
    sinopsis = models.TextField()
    actores = models.TextField()
    
    def __str__(self):
        return self.titulo

    
