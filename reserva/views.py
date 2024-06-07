from django.templatetags.static import static
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import FileResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from .models import Sala, Entrada, Sesion, Sillon
from .serializers import SesionSerializer, SesionListSerializer, SalaSerializer, EntradaSerializer, EntradaListSerializer, SillonSerializer, SalaListSerializer
# Create your views here.

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["hora", "id" , "pelicula__id", "sala__id"]
    
    action_serializers = {
        "retrieve": SesionListSerializer,
        "list":SesionListSerializer,
        'create':SesionSerializer,
        'update':SesionSerializer
    }
    
    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(SesionViewSet, self).get_serializer_class()
    
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ "id" , "usuario__id"]
    
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
    
    
def imprimirEntrada(request):
    
    url = static("entrada.html")
    print(url)
    return Response(open(url))