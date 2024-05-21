from django.db import models

# Aqui iran los modelos relacionados con la compra de comidas, menus y refrigerios.

#Comidas que puedes comprar (palomitas, hamburguesas, bolsas de chuches, etc.)
class Comida(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    foto = models.ImageField()
    precio = models.FloatField()

#Bebidas que puedes comprar (cocacola, fanta, agua, etc.)
class Bebida(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    foto = models.ImageField()
    precio = models.FloatField()
    
#Menus que puedes comprar (menu pareja, menu familiar, menu obesidad, etc.)
class Menu(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    id_comida = models.ForeignKey(Comida, on_delete=models.CASCADE)
    id_bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    foto = models.ImageField()
    precio = models.FloatField()
