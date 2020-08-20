from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from miapp.models import cursos, carreras , estudiantes
from django.shortcuts import render
from .forms import consultar

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def consultas(request):
    form = consultar()

    return render(request, 'consultas.html', {'form': form})

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

def listar_estudiantes(request):
    alumno = estudiantes.objects.all()
    
    return render(request, 'estudiantes.html',{
        'estudiantes': alumno,
        'titulo': 'Listado de estudiantes'
    })

def eliminar_estudiante(request, id):
    alumno=estudiantes.objects.get(pk=id)
    alumno.delete()

    return redirect('Estudiantes')