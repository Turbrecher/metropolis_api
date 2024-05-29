from django.urls import re_path
from .views import PeliculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register("api/peliculas", PeliculaViewSet)

urlpatterns = router.urls
