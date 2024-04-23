from .models import Pelicula, PeliculaGenero, Pegi, Genero, Actor, Interpretacion
from rest_framework import viewsets, permissions
from .serializers import PeliculaSerializer, PeliculaGeneroSerializer, PegiSerializer, GeneroSerializer, ActorSerializer, InterpretacionSerializer

#Vista de API Pelicula
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeliculaSerializer
    
#Vista de API PeliculaGenero
class PeliculaGeneroViewSet(viewsets.ModelViewSet):
    queryset = PeliculaGenero.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PeliculaGeneroSerializer
    
    
#Vista de API Pegi
class PegiViewSet(viewsets.ModelViewSet):
    queryset = Pegi.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PegiSerializer
    
#Vista de API Genero
class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GeneroSerializer
    
#Vista de API Actor
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ActorSerializer
    
#Vista de API Interpretacion
class InterpretacionViewSet(viewsets.ModelViewSet):
    queryset = Interpretacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InterpretacionSerializer