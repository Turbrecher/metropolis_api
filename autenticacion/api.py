from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer
from .models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer