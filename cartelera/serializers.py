from rest_framework import serializers
from .models import Pelicula
     
#Serializador de peliculas   
class PeliculaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pelicula
        fields = serializers.ALL_FIELDS
        read_only_fields = ('id',)
        
