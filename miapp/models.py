from django.db import models

# Create your models here.

class cursos(models.Model):
    idcurso = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True,max_length=10)
    nombre = models.CharField(max_length=100)
    horas = models.IntegerField()
    creditos = models.IntegerField()
    estados = models.CharField(max_length=1)  



