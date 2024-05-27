from .api import PeliculaViewSet, PeliculaGeneroViewSet, GeneroViewSet, PegiViewSet, ActorViewSet, InterpretacionViewSet
from rest_framework import routers



router = routers.DefaultRouter()

router.register('api/peliculas', PeliculaViewSet, 'peliculas')
router.register('api/generos', GeneroViewSet, 'generos')
router.register('api/pegis', PegiViewSet, 'pegis')
router.register('api/actores', ActorViewSet, 'actores')
router.register('api/peliculasgeneros', PeliculaGeneroViewSet, 'peliculasgeneros')
router.register('api/interpretaciones', InterpretacionViewSet, 'interpretaciones')


urlpatterns = router.urls
