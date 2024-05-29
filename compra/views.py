from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .serializers import ComidaSerializer, BebidaSerializer, MenuListSerializer, MenuSerializer, TipoEntradaSerializer
from .models import Comida, Bebida, Menu, TipoEntrada


class TipoEntradaViewSet(viewsets.ModelViewSet):
    serializer_class = TipoEntradaSerializer
    queryset = TipoEntrada.objects.all()

#---------COMIDAS--------------
class ComidaViewSet(viewsets.ModelViewSet):
    serializer_class = ComidaSerializer
    queryset = Comida.objects.all()
    
#---------BEBIDAS--------------
class BebidaViewSet(viewsets.ModelViewSet):
    serializer_class = BebidaSerializer
    queryset = Bebida.objects.all()
    

#---------MENUS--------------
class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
    def list(self, request):
        queryset = Menu.objects.all()
        
        #Si el usuario filtra por id de comida
        id_comida = request.GET.get("id_bebida")
        if id_comida is not None:
            #Filtramos por id de pelicula
            queryset = Menu.objects.filter(comida_id = id_comida)
            
        #Si el usuario filtra por id de bebida
        id_bebida = request.GET.get("id_bebida")
        if id_bebida is not None:
            #Filtramos por id de pelicula
            queryset = Menu.objects.filter(bebida_id = id_bebida)
            
        serializer = MenuListSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Menu.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MenuListSerializer(user, many=False)
        
        return Response(serializer.data)
    

