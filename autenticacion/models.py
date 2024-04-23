from django.db import models

# Aqui iran los modelos relacionados con la autenticacion de usuarios.

class Usuario(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    email = models.TextField()
    fecha_nacimiento = models.DateField()
    password = models.TextField()
    es_admin = models.BooleanField()
    
