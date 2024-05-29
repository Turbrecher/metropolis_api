from rest_framework import routers
from .views import ComidaViewSet, BebidaViewSet, MenuViewSet, TipoEntradaViewSet
from django.urls import re_path

router = routers.DefaultRouter()

router.register("api/comidas", ComidaViewSet),
router.register("api/bebidas", BebidaViewSet),
router.register("api/menus", MenuViewSet),
router.register("api/tiposentrada", TipoEntradaViewSet),


urlpatterns = router.get_urls()