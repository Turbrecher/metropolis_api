from rest_framework import serializers
from .models import Sala, Entrada, Sesion
from autenticacion.serializers import UserSerializer
from cartelera.serializers import PeliculaSerializer

#Serializador del modelo Sala
class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)

#Serializador del modelo Sesion para todo menos listar
class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields =  "__all__"
        
#Serializador del modelo Sesion para listar
class SesionListSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(many=False)
    pelicula = PeliculaSerializer(many=False)
    
    class Meta:
        model = Sesion
        fields =  "__all__"
        

        
#Serializador del modelo Entrada    
class EntradaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Entrada
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
#Serializador del modelo Entrada para listas 
class EntradaListSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(many=False, read_only=True)
    sesion = SesionListSerializer(many=False, read_only=True)
    
    class Meta:
        model = Entrada
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)