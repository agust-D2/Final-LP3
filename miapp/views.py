from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from miapp.models import cursos, carreras


# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def estudiantes(request):
    return render(request, 'estudiantes.html')
def consultas(request):
    return render(request, 'consultas.html')

def listar_cursos(request):
    curso = cursos.objects.all()
    
    return render(request, 'cursos.html',{
        'cursos': curso,
        'titulo': 'Listado de Cursos'
    })

def eliminar_cursos(request, id):
    curso =cursos.objects.get(pk=id)
    curso.delete()

    return redirect('cursos')

def listar_carreras(request):
    carr = carreras.objects.all()
    
    return render(request, 'carreras.html',{
        'carrera': carr,
        'titulo': 'Listado de carreras'
    })

def eliminar_carreras(request, id):
    carr =carreras.objects.get(pk=id)
    carr.delete()

    return redirect('carreras')