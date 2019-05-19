from django.db import models
import datetime

# Create your models here.
class IntegerRangeField(models.IntegerField):
    def init(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.init(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Partido_politico(models.Model):
    """Clase que guarda una cadena de texto con el nombre del Partido"""
    Nombre = models.CharField(max_length = 256)
    def str(self):
        return self.Nombre
class Candidato(models.Model):
    """Clase que guarda una cadena de texto con el nombre del candidato y su partido"""
    Nombre = models.CharField(max_length = 256)
    Partido = models.ForeignKey(Partido_politico, on_delete = models.CASCADE)#ForeignKey dependencia con otra tabla

    def str(self):
        return self.Nombre
class Voto(models.Model):
    """Clase que crea el voto con la fecha de las elecciones"""
    Fecha = models.DateTimeField(auto_now = True)
    Candidato = models.ForeignKey(Candidato, on_delete = models.CASCADE)
    votes = IntegerRangeField(min_value = 1, max_value =1)
#    FechaNacimiento = models.DateField()
    def str(self):
        return "Voto por el Candidato: {1}".format(self.Fecha, self.Candidato)
class Votante(models.Model):

#Clase que crea una cadena de texto con el nombre del votante, documento, correo y el voto"""

    Nombre = models.CharField(max_length = 256)
    Documento = models.CharField(max_length = 10 )
    Email = models.EmailField(max_length = 256)
    Voto = models.ForeignKey(Voto, on_delete = models.CASCADE)
    FechaNacimiento = models.DateField()
    Sexos = (('F','Femenino'),('M','Masculino'),('O','Otro'))
    Sexo = models.CharField(max_length = 1, choices= Sexos, default= 'M')
   """ def inf_votante(self):
        cadena = "NOMBRE: {0} , Documento:{1} , FechaNacimiento: {2} , correo:{3}"
        return cadena.format(self.Nombre,slef.Documento,self.FechaNacimiento,self.Email)"""
    def str(self):
        return "Nombre: {0} , Documento:{1} , FechaNacimiento: {2} , correo:{3}".format(self.Nombre,self.Documento,self.FechaNacimiento,self.Email)
"""class Resultados(models.Model):
    votos_totales = models.ForeignKey(Voto, on_delete = models.CASCADE)
    candidato_votos = models.ForeignKey(Candidato, on_delete = models.CASCADE)
    def str(self):
        return "El candidato : {0} tiene {1} vostos".formart(self.nombre,self.votes)"""
