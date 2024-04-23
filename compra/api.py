from rest_framework import viewsets, permissions
from .models import Comida, Bebida, Menu
from .serializers import ComidaSerializer, BebidaSerializer, MenuSerializer

#Vista de comida
class ComidaViewSet(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ComidaSerializer
    
    
#Vista de bebidas
class BebidaViewSet(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BebidaSerializer
    
#Vista de menus
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MenuSerializer