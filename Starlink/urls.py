import imp
from django.shortcuts import redirect
from django.urls import path
from Starlink import views

urlpatterns = [
    path('', views.start, name = "start"),
    path('Peliculas', views.start, name = "ver_peliculas"),
    path('Agregar', views.agregar, name = "agregar"),
    path('Borrar_<int:id>', views.borrar, name = "borrar"),
    path('Modificar_<int:id>', views.modificar, name = "modificar"),
    path('Hija1', views.hija1 , name = "hija1"),
    path('Peliculasbd', views.peliculasbd, name = "peliculasbd"),
    path('Borrarbd_<int:id>', views.borrarbd, name = "borrarbd"),
    path("Agragarbd", views.agregarbd, name="agregarbd"),
]
