from django.urls import path
from WebDjango.views import *



urlpatterns = [
    path("inicio/", inicio, name="proyecto-inicio"),
    path("peliculas/", Pelicula, name="proyecto-peliculas"),
    path("peliculas/crear/", creacion_pelicula, name="proyecto-peliculas-crear"),
    path("peliculas/buscar/", buscar_pelicula, name="proyecto-peliculas-buscar"),
    path("peliculas/buscar/resultados", resultados_busqueda_peliculas, name="proyecto-peliculas-buscar-resultados"),
    path("series/", series, name="proyecto-series"),
    path("series/crear/", creacion_serie, name="proyecto-series-crear"),
    path("series/buscar/", buscar_serie, name="proyecto-serie-buscar"),
    path("series/buscar/resultados", resultados_busqueda_series, name="proyecto-series-buscar-resultados"),
    path("music/", musica, name="proyecto-music"),
    path("music/crear/", creacion_musica, name="proyecto-music-crear"),
    path("music/buscar/", buscar_musica, name="proyecto-music-buscar"),
    path("music/buscar/resultados", resultados_busqueda_musica, name="proyecto-music-buscar-resultados"),


]