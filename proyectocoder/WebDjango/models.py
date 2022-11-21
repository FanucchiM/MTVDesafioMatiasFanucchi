from django.db import models

# Create your models here.
class peliculas(models.Model):

    nombre=models.CharField(max_length=40)
    genero=models.CharField(max_length=18)
    duracion_en_minutos=models.CharField(max_length=25)
    

class music(models.Model):

    
    duracion_de_la_cancion_en_minutos=models.IntegerField()
    cantante=models.CharField(max_length=15)

class serie(models.Model):

    nombre=models.CharField(max_length=20)
    temporadas=models.IntegerField()
    genero=models.CharField(max_length=23)


