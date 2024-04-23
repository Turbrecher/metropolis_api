from django.contrib import admin
from django.urls import path
from cartelera import views

urlpatterns = [
    path('cartelera/', views.cartelera ),
]