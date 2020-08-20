"""LP3FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('cursos/', views.listar_cursos, name="cursos"),
    path('carreras/',views.listar_carreras, name="carreras"),
    path('Estudiantes/',views.listar_estudiantes, name="Estudiantes"),
    path('Consultas/',views.consultas, name="Consultas"),
    path('eliminar-cursos/<int:id>',views.eliminar_cursos, name="eliminar_cursos"),
    path('eliminar-carreras/<int:id>',views.eliminar_carreras, name="eliminar_carreras"),
    path('eliminar-estudiante/<int:id>',views.eliminar_estudiante, name="eliminar_estudiante"),


]
