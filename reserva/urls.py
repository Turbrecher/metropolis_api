from django.urls import path,re_path
from rest_framework import routers
from .views import SesionViewSet, EntradaViewSet, SalaViewSet

router = routers.DefaultRouter()
router.register("api/sesiones", SesionViewSet)
router.register("api/entradas", EntradaViewSet)
router.register("api/salas", SalaViewSet)



urlpatterns = router.get_urls()