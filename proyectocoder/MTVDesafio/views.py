from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from MTVDesafio.models import Familiares


# Create your views here.


def listadoFamiliares(request):

    listaFamiliares = Familiares.objects.all()
    
    datos = {
        "listaFamiliares": listaFamiliares,

    }    
    plantilla = loader.get_template("familia.html")    
    
    documento =  plantilla.render(datos)    
    
    return HttpResponse(documento)