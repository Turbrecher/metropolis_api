from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .serializers import UserSerializer, AdminUserSerializer
from django.core import serializers

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets, permissions, generics

from django.contrib.auth.models import User


#VIEWSET GENERAL PARA LISTAR, SUBIR, EDITAR Y ELIMINAR
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = AdminUserSerializer
    queryset = User.objects.all()


#APIS PARA REGISTRO, LOGIN Y PERFIL DE USUARIO

@api_view(['POST'])
def login(request):
    
    user = get_object_or_404(User, username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({'error':'Invalid password', 'status':status.HTTP_400_BAD_REQUEST})
    
    token,created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    
    return Response({'token':token.key, 'user':serializer.data, 'status':status.HTTP_200_OK})


@api_view(['POST'])
def register(request):
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
        user = User.objects.get(username = serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        
        token = Token.objects.create(user=user)
        return Response({'token':token.key, 'user':serializer.data, 'status':status.HTTP_201_CREATED})
    
    
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_user(request):
    
    serializer = AdminUserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
        user = User.objects.get(username = serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.is_superuser = (serializer.data["is_superuser"])
        user.save()
        
        token = Token.objects.create(user=user)
        print(token)
        print(serializer.data["is_superuser"])
        return Response({'token':token.key, 'user':serializer.data, 'status':status.HTTP_201_CREATED})
    
    
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def edit(request):
    
    user = User.objects.get(id = request.data['id'])
    
    if user:
        user.email =  request.data['email']
        user.first_name =  request.data['first_name']
        user.last_name =  request.data['last_name']
        
        if (request.data["password"] == request.data["confirm_password"]) and len(request.data["password"]) >= 8 :
            user.set_password(request.data['password'])
        
        user.save()
        return Response({'user':request.data, 'status':status.HTTP_201_CREATED})       
    
    return Response("No se ha podido guardar el usuario", status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    
    serializer = UserSerializer(instance=request.user)
    
    serializerAdmin = AdminUserSerializer(instance=request.user)
    
    if(serializerAdmin.data.get("is_superuser") == True):
        return Response(serializerAdmin.data ,status=status.HTTP_200_OK)
    
    
    return Response(serializer.data ,status=status.HTTP_200_OK)
