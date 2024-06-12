from django.urls import path,re_path
from rest_framework import routers
from .views import SesionViewSet, EntradaViewSet, SalaViewSet, SillonViewSet, imprimirEntrada, getEntrada
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register("api/sesiones", SesionViewSet)
router.register("api/entradas", EntradaViewSet)
router.register("api/salas", SalaViewSet)
router.register("api/sillones", SillonViewSet)



urlpatterns = [
    path("entradas/descargar/<int:id>/", imprimirEntrada),
    path("entradas/ver/<int:id>/", getEntrada),
] + router.get_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
