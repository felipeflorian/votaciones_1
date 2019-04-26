from django.db import models

# Create your models here.
class Partido_politico(models.Model):
    """Clase que guarda una cadena de texto con el nombre del Partido"""
    Nombre = models.CharField(max_length = 256)
class Candidato(models.Model):
    """Clase que guarda una cadena de texto con el nombre del candidato y su partido"""
    Nombre = models.CharField(max_length = 256)
    Partido = models.ForeignKey(Partido_politico, on_delete = models.CASCADE)#ForeignKey dependencia con otra tabla
class Voto(models.Model):
    """Clase que crea el voto con la fecha de las elecciones"""
    Fecha = models.DateTimeField(auto_now = True)
    Candidato = models.ForeignKey(Candidato, on_delete = models.CASCADE)
class Votante(models.Model):
    """Clase que crea una cadena de texto con el nombre del votante, documento, correo y el voto """
    Nombre = models.CharField(max_length = 256)
    Documento = models.CharField(max_length = 10 )
    Email = models.EmailField(max_length = 256)
    Voto = models.ForeignKey(Voto, on_delete = models.CASCADE)

