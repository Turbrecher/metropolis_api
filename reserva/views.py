from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions, viewsets, status
from .models import Sala, Entrada, Sesion, Sillon
from .serializers import SesionSerializer, SesionListSerializer, SalaSerializer, EntradaSerializer, EntradaListSerializer, SillonSerializer, SalaListSerializer
# Create your views here.

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer
    
    def list(self, request):
        queryset = Sesion.objects.all()
        
        
        #Si el usuario filtra por id de pelicula
        id_pelicula = request.GET.get("pelicula__id")
        if id_pelicula is not None:
            #Filtramos por id de pelicula
            queryset = Sesion.objects.filter(pelicula__id = id_pelicula)
            
        #Si el usuario filtra por id de sala
        id_sala = request.GET.get("sala__id")
        if id_sala is not None:
            #Filtramos por id de pelicula
            queryset = Sesion.objects.filter(sala__id = id_sala)
            
        serializer = SesionListSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Sesion.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SesionListSerializer(user, many=False)
        
        return Response(serializer.data)
    
class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    
    action_serializers = {
        "retrieve": SalaListSerializer,
        "list":SalaListSerializer,
        'create':SalaSerializer,
        'update':SalaSerializer
    }
    
    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(SalaViewSet, self).get_serializer_class()
      
    
class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    
    action_serializers = {
        "retrieve": EntradaListSerializer,
        "list":EntradaListSerializer,
        'create':EntradaSerializer,
        'update':EntradaSerializer
    }
    
    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(EntradaViewSet, self).get_serializer_class()
    
class SillonViewSet(viewsets.ModelViewSet):
    queryset = Sillon.objects.all()
    serializer_class = SillonSerializer