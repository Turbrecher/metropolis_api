from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacion/', include('autenticacion.urls'), name='autenticacion'),
    path('cartelera/', include('cartelera.urls'), name='cartelera'),
    path('compra/', include('compra.urls'), name='compra'),
    path('reserva/', include('reserva.urls'), name='reserva'),
    
    
    
] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#para la carga de imagenes
