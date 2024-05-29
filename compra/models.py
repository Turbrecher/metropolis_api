from django.db import models

# Aqui iran los modelos relacionados con la compra de comidas, menus y refrigerios.

#Comidas que puedes comprar (palomitas, hamburguesas, bolsas de chuches, etc.)
class Comida(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    foto = models.ImageField()
    precio = models.FloatField()
    
    def __str__(self):
        return self.nombre

#Bebidas que puedes comprar (cocacola, fanta, agua, etc.)
class Bebida(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    foto = models.ImageField()
    precio = models.FloatField()
    
    def __str__(self):
        return self.nombre
    
#Menus que puedes comprar (menu pareja, menu familiar, menu obesidad, etc.)
class Menu(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    foto = models.ImageField()
    precio = models.FloatField()
    
    def __str__(self):
        return self.nombre
    
class TipoEntrada(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    foto = models.ImageField()
    precio = models.FloatField()
