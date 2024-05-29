from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions, viewsets, status
from .models import Sala, Entrada, Sesion
from .serializers import SesionSerializer, SesionListSerializer, SalaSerializer, EntradaSerializer, EntradaListSerializer
# Create your views here.

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer
    
    def list(self, request):
        queryset = Sesion.objects.all()
        
        #Si el usuario filtra por id de pelicula
        id_pelicula = request.GET.get("id_pelicula")
        if id_pelicula is not None:
            #Filtramos por id de pelicula
            queryset = Sesion.objects.filter(id_pelicula = id_pelicula)
            
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
    
class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    
    def list(self, request):
        queryset = Entrada.objects.all()
        
        #Si el usuario filtra por id de usuario
        id_usuario = request.GET.get("id_usuario")
        if id_usuario is not None:
            #Filtramos por id de usuario
            queryset = Entrada.objects.filter(usuario_id = id_usuario)
            
        #Si el usuario filtra por id de sesion
        id_sesion = request.GET.get("id_sesion")
        if id_sesion is not None:
            #Filtramos por id de usuario
            queryset = Entrada.objects.filter(sesion_id = id_sesion)
            
        serializer = EntradaListSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Entrada.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EntradaListSerializer(user, many=False)
        
        return Response(serializer.data)