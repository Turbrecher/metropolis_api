from rest_framework import routers
from .api import ComidaViewSet, BebidaViewSet, MenuViewSet

router = routers.DefaultRouter()

router.register('api/comidas', ComidaViewSet, 'comidas')
router.register('api/bebidas', BebidaViewSet, 'bebidas')
router.register('api/menus', MenuViewSet, 'menus')

urlpatterns = router.urls