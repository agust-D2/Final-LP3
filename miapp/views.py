from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from miapp.models import cursos

# Create your views here.

def index(request):
    return render(request, 'index.html')

def carreras(request):
    return render(request, 'carreras.html')
def estudiantes(request):
    return render(request, 'estudiantes.html')
def consultas(request):
    return render(request, 'consultas.html')

def listar_cursos(request):
    curso = cursos.objects.all()
    
    return render(request, 'cursos.html',{
        'cursos': curso,
        'titulo': 'listado de Cursos'
    })

def eliminar_cursos(request, id):
    curso =cursos.objects.get(pk=id)
    curso.delete()

    return redirect('cursos')