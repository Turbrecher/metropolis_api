from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .serializers import ComidaSerializer, BebidaSerializer, MenuListSerializer, MenuSerializer, TipoEntradaSerializer
from .models import Comida, Bebida, Menu, TipoEntrada


class TipoEntradaViewSet(viewsets.ModelViewSet):
    serializer_class = TipoEntradaSerializer
    queryset = TipoEntrada.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nombre", "id"]
        

#---------COMIDAS--------------
class ComidaViewSet(viewsets.ModelViewSet):
    serializer_class = ComidaSerializer
    queryset = Comida.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nombre", "id", "descripcion", "precio"]
    
#---------BEBIDAS--------------
class BebidaViewSet(viewsets.ModelViewSet):
    serializer_class = BebidaSerializer
    queryset = Bebida.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nombre", "id", "descripcion", "precio"]
    

#---------MENUS--------------
class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nombre", "id", "descripcion", "precio"]
    
    action_serializers = {
        "retrieve": MenuListSerializer,
        "list":MenuListSerializer,
        'create':MenuSerializer,
        'update':MenuSerializer
    }
    
    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(MenuViewSet, self).get_serializer_class()
    
    
    

