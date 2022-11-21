from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from appcoder.models import Curso, Profesor, Estudiante
from django.shortcuts import render
from appcoder.forms import ProfesorFormulario



def inicio(request):
    return render(request, "appcoder/index.html")

def creacion_curso(request):
    
    if request.method=="POST":
        nombre_curso=request.POST["curso"]
        numero_camada=request.POST["camada"]

        curso= Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()
        
    return render(request, "appcoder/curso_formulario.html")
    
def cursos(request):
    return render(request, "appcoder/cursos.html")
    
def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")
    
def profesores(request):
    return render(request, "appcoder/profesores.html")

def creacion_profesores(request):

    if request.method=="POST":
        formulario=ProfesorFormulario()

        #Validamos  que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor=Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])

            profesor.save()

        return render(request, "appcoder/index.html")

    formulario=ProfesorFormulario()
    contexto={"formulario": formulario}
    return render(request, "appcoder/profesores_formularios.html", contexto)



def buscar_curso(request):

    return render(request, "appcoder/busqueda_cursos.html")
    
def resultados_busqueda_cursos(request):
    nombre_curso = request.GET["Nombre_curso"]

    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "appcoder/resultados_busquedas_cursos.html", {"cursos": cursos})
    
    
def entregables(request):
    return render(request, "appcoder/entregables.html")