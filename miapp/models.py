from django.db import models

# Create your models here.

class cursos(models.Model):
    idcurso = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True,max_length=10)
    nombre = models.CharField(max_length=100)
    horas = models.IntegerField()
    creditos = models.IntegerField()
    estados = models.CharField(max_length=1)  

class carreras(models.Model):
    idcarrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nombrecorto = models.CharField(max_length=10)
    fecha_fundacion = models.CharField(max_length=20)
    estado = models.CharField(max_length=1)

class estudiantes(models.Model):
    idestudiante = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True,max_length=10)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=20)
    estado = models.CharField(max_length=1)



