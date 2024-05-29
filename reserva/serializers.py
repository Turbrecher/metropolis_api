from rest_framework import serializers
from .models import Sala, Entrada, Sesion, Sillon
from autenticacion.serializers import UserSerializer
from cartelera.serializers import PeliculaSerializer
from compra.serializers import TipoEntradaSerializer


class SillonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sillon
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)

#Serializador del modelo Sala
class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
#Serializador del modelo Sala
class SalaListSerializer(serializers.ModelSerializer):
    sillones = SillonSerializer(many=True)
    
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
    sala = SalaListSerializer(many=False)
    pelicula = PeliculaSerializer(many=False)
    sillones_ocupados = SillonSerializer(many=True)
    
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
    tipo_entrada = TipoEntradaSerializer(many=False, read_only=True)
    
    class Meta:
        model = Entrada
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)