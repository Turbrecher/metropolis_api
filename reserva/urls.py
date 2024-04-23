from rest_framework import routers
from .api import SalaViewSet, EntradaViewSet, SesionViewSet

router = routers.DefaultRouter()

router.register('api/salas', SalaViewSet, 'salas')
router.register('api/entradas', EntradaViewSet, 'entradas')
router.register('api/sesiones', SesionViewSet, 'sesiones')

urlpatterns = router.urls