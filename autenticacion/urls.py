from .views import register,login,profile, edit,create_user, UserViewSet
from rest_framework import routers
from django.urls import  re_path

router = routers.DefaultRouter()

router.register("api/usuarios",UserViewSet)


urlpatterns = [
    re_path('api/usuarios/register', register, name = 'register'),
    re_path('api/usuarios/login', login, name = 'login'),
    re_path('api/usuarios/profile', profile, name = 'profile'),
    re_path('api/usuarios/edit', edit, name = 'edit'),
    re_path('api/usuarios/create', create_user, name = 'create'),
    ] + router.get_urls()