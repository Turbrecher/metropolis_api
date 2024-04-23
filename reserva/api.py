from rest_framework import viewsets, permissions
from .serializers import SalaSerializer, EntradaSerializer, SesionSerializer
from .models import Sala, Entrada, Sesion

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SalaSerializer
    
class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EntradaSerializer
    
class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SesionSerializer