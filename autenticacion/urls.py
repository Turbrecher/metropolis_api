from .api import UsuarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/usuarios', UsuarioViewSet, 'usuarios')

urlpatterns = router.urls