from ast import Return
import re
from urllib import request
from django.shortcuts import redirect, render
from django import forms

from .models import Peliculas
# Create your views here.

#creación de una lista
peliculas = [
    {
        "titulo" : "Spider-Man" ,
        "year" : 2001,
        "bio": "Marvel Comics. Grupos. Spider-Man. Sinopsis. Tras la muerte de sus padres, Peter Parker, un tímido estudiante, vive con su tía May y su tío Ben. Precisamente debido a su retraimiento no es un chico muy popular en el instituto."
    },
    {
        "titulo" : "Deadpool",
        "year" : 2016, 
        "bio" : "Grupos. X-Men | Deadpool. Sinopsis. Basado en el anti-héroe menos convencional de la Marvel, Deadpool narra el origen de un ex-operativo de la fuerzas especiales llamado Wade Wilson, reconvertido a mercenario, y que tras ser sometido a un cruel experimento adquiere poderes de curación rápida, adoptando Wade entonces el alter ego de Deadpool."
    },
]
#metodo de inicio de la página web
def start(request):
    return render(
        request, 
        'start.html',
        {
            "valor" : 10, 
            "peliculas":peliculas
        }
    )

#metodo para agregar datos
def agregar(request):
    if request.method == "POST":
        #guarda los datos insertados en el input
        peliculas.append(
            {
                "titulo":request.POST['titulo'],
                "year":int(request.POST['year']),
                "bio":request.POST['bio']
            }
        )
        #envia directo  al a página web al guardar
        return redirect('start')
    return render(request,'agregar.html',{})

#metodo para borrar
def borrar(request, id):
    #el ".pop" sirve para remover una sección de la lista
    peliculas.pop(id);
    return render(request, "start.html",{"peliculas":peliculas})

#metodo para modificar
def modificar(request, id):

    #si el metodo es igual a POST
    if request.method == "POST":
        #pasar los datos a los input para modificarlos y guardarlos
        peliculas[id] = {
            "titulo":request.POST['titulo'],
            "year":int(request.POST['year']),
            "bio":request.POST['bio']
        }
        #envia directo  al a página web al guardar
        return redirect('start')
    #regresa y muestra los nuevos datos
    return render(
        request, 
        "modificar.html",
        {
            "titulo":peliculas[id]["titulo"],
            "year":peliculas[id]["year"],
            "bio":peliculas[id]["bio"], 
            "id": id
        }
    ),

def hija1(request):
    return render(request,'hija1.html',{})

def peliculasbd(request):
    return render(request, 'peliculasbd.html', {"pelisbd": Peliculas.objects.all()})

def borrarbd(request, id):
    peli = Peliculas.objects.get(id = id)
    peli.delete()
    return redirect("peliculasbd")

def agregarbd(request):
    if request.method == "POST":
        p = Peliculas(
            title = request.POST["title"],
            year = int(request.POST["year"])
        )
        p.save()
        return redirect("peliculasbd")
    return render(request, "agregarbd.html", {})


    