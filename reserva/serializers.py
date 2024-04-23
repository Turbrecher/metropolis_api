from rest_framework import serializers
from .models import Sala, Entrada, Sesion

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)