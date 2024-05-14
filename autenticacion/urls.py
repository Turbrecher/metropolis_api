from .api import UsuarioViewSet
from .views import register,login,profile
from rest_framework import routers
from django.urls import path, re_path

router = routers.DefaultRouter()

router.register('api/usuarios', UsuarioViewSet, 'usuarios')

urlpatterns = [
    re_path('api/usuarios/register', register, name = 'register'),
    re_path('api/usuarios/login', login, name = 'login'),
    re_path('api/usuarios/profile', profile, name = 'profile'),
    ]