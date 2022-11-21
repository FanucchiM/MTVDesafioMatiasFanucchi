from django import forms


class PeliculaFormulario(forms.Form):

    nombre=forms.CharField()
    genero=forms.CharField()
    duracion_en_minutos=forms.CharField()
    estreno=forms.IntegerField()

class SerieFormulario(forms.Form):

    nombre=forms.CharField()
    genero=forms.CharField()
    temporadas=forms.CharField()
    estreno=forms.IntegerField()
    capitulos=forms.IntegerField()

class MusicaFormulario(forms.Form):

    duracion_de_la_cancion_en_minutos=forms.IntegerField()
    cantante=forms.CharField()
    nombre_cancion=forms.CharField()