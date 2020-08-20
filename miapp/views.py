from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'index.html')
def cursos(request):
    return render(request, 'cursos.html')
def carreras(request):
    return render(request, 'carreras.html')
def estudiantes(request):
    return render(request, 'estudiantes.html')
def consultas(request):
    return render(request, 'consultas.html')