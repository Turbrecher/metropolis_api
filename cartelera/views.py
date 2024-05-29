from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Pelicula
from rest_framework import viewsets, permissions,filters,generics
from .serializers import PeliculaSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer