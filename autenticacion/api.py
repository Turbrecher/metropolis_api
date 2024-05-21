from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer