from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from WebDjango.models import *
from WebDjango.forms import *
# Create your views here.



def inicio(request):
    return render(request, "WebDjango/inicio.html")


def Pelicula(request):

    return render(request, "WebDjango/peliculas.html")


def creacion_pelicula(request):

    if request.method== "POST":
        formulario=PeliculaFormulario(request.POST)
        
        #Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            pelicula=peliculas(nombre=data["nombre"], genero=data["genero"], duracion_en_minutos=data["duracion_en_minutos"])
            pelicula.save()
        return render (request, "WebDjango/inicio.html")
    
    formulario=PeliculaFormulario()

    contexto= {"formulario": formulario}
    return render (request, "WebDjango/peliculas_formularios.html", contexto)

def buscar_pelicula(request):

    return render(request, "WebDjango/busqueda_peliculas.html")

def resultados_busqueda_peliculas(request):
    nombre_pelicula = request.GET["nombre_pelicula"]

    zxc = peliculas.objects.filter(nombre__icontains=nombre_pelicula)
    return render(request, "WebDjango/resultados_busquedas_peliculas.html", {"Pelicula": zxc})

def resultados_busqueda_musica(request):

    a_music = request.GET["nombre_musica"]

    asdf = music.objects.filter(cantante__icontains=a_music)
    return render(request, "WebDjango/resultados_busquedas_musica.html", {"musica": asdf})

def musica(request):

    return render(request, "WebDjango/music.html")



def creacion_musica(request):

    if request.method== "POST":
        formulario=MusicaFormulario(request.POST)
        
        #Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            musicas=music(duracion_de_la_cancion_en_minutos=data["duracion_de_la_cancion_en_minutos"], cantante=data["cantante"])
            musicas.save()
        return render (request, "WebDjango/inicio.html")
    
    formulario=MusicaFormulario()

    contexto= {"formulario": formulario}
    return render (request, "WebDjango/musica_formularios.html", contexto)

def buscar_musica(request):

    return render(request, "WebDjango/busqueda_musica.html")




def resultados_busqueda_series(request):

    nombre_serie = request.GET["nombre_serie"]

    asd = serie.objects.filter(nombre__icontains=nombre_serie)
    return render(request, "WebDjango/resultados_busquedas_series.html", {"series": asd})



def series(request):

    return render(request, "WebDjango/series.html")

    
def creacion_serie(request):

    if request.method== "POST":
        formulario=SerieFormulario(request.POST)
        
        #Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            series=serie(nombre=data["nombre"], temporadas=data["temporadas"], genero=data["genero"])
            series.save()
        return render (request, "WebDjango/inicio.html")
    
    formulario=SerieFormulario()

    contexto= {"formulario": formulario}
    return render (request, "WebDjango/series_formularios.html", contexto)

def buscar_serie(request):

    return render(request, "WebDjango/busqueda_series.html")





