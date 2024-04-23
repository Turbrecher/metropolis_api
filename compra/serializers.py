from rest_framework import serializers
from .models import Comida, Bebida, Menu

#Serializador del modelo Comida
class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
#Serializador del modelo Bebida
class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebida
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
#Serializador del modelo Menu
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)