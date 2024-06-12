import string
from weasyprint import HTML
from django.templatetags.static import static
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import FileResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from .models import Sala, Entrada, Sesion, Sillon
from cartelera.models import Pelicula
from django.contrib.auth.models import User
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
    
    
def getEntrada(request, id):
    
    #Obtenemos entrada
    entrada = Entrada.objects.filter(id=id)[0]
    precio = str(entrada.tipo_entrada).rsplit("/")[1].strip()
    
    #Obtenemos usuario
    username = str(entrada.usuario).strip()
    usuario = User.objects.filter(username=username)[0]
    
    #COMPROBAR LUEGO AUTENTICACION
    
    #Obtenemos la hora de la sesion
    hora = str(entrada.sesion).rsplit("//")[1].strip() + "0"
    
    #Obtenemos la pelicula
    titulo_pelicula =  str(entrada.sesion).rsplit("//")[0].strip()
    pelicula = Pelicula.objects.filter(titulo = titulo_pelicula)[0]

    #Obtenemos la sesion
    sesion = Sesion.objects.filter(hora= (hora), pelicula=pelicula.id)[0]
    
    #Obtenemos el nombre de la sala
    sala = sesion.sala
    
    #Obtenemos el logotipo
    logotipo = static("metropolis_logo.png")
    
    #Obtenemos el qr
    qr_code = static("qr_code.png")
    
    #Obtenemos la metropolis
    metropolis = static("metropolis.png")
    
    
    return render(template_name="entrada.html", request=request, context={
        "usuario":usuario,
        "entrada":entrada,
        "hora":hora,
        "titulo_pelicula":titulo_pelicula,
        "sala":sala,
        "precio":precio,
        "logotipo":logotipo,
        "qr_code":qr_code,
        "metropolis":metropolis
    })
    
def imprimirEntrada(request, id):
    url = "http://localhost:8000/reserva/entradas/ver/"+str(id)
    pdf = HTML(url = url).write_pdf(target='reserva/templates/entrada_factura.pdf')
    
    return FileResponse(open('reserva/templates/entrada_factura.pdf', 'rb'), content_type='application/pdf')