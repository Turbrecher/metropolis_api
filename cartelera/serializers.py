from rest_framework import serializers
from .models import Pelicula, PeliculaGenero, Genero, Pegi, Actor, Interpretacion


#Serializador de Generos
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
    
#Serializador de Pegis    
class PegiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pegi
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
     
#Serializador de peliculas   
class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
#Serializador de PeliculaGenero
class PeliculaGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeliculaGenero
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
#Serializador de Actores
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
#Serializador de Interpretaciones
class InterpretacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpretacion
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)