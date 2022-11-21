from django.db import models

# Create your models here.

# Se crea la clase Familiares para luego ser migrada como tabla en sqlite
class Familiares(models.Model):

    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha = models.DateField()
    

    
