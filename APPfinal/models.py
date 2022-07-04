from django.db import models
from django.utils import timezone

# Create your models here.
choices = [
    ['Apostilla', 'Apostilla'],
    ['Partidas', 'Partidas'],
    ['Residencia Uruguaya', 'Residencia Uruguaya'],
    ['Titulos de Estudio', 'Titulos de Estudio'],
    ['DNI', 'DNI'],
    ['Pasaporte', 'Pasaporte'],
    ['Turnos visados', 'Turnos visados'],
    ['Otro', 'Otro'],
 

]
class ModeloCliente(models.Model):

    nombre = models.CharField(max_length=40, null=False)
    apellido = models.CharField(max_length=40, null=False)
    email = models.EmailField(null=False)
    documentos = models.BooleanField(default=False)
    fecha_creado = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido

class ModeloTramite(models.Model):

    tramite = models.CharField(max_length=40, choices=choices)

    def __str__(self) -> str:
        return self.tramite

class ModeloFecha(models.Model):

    dia = models.CharField(max_length=40, null=False)
    mes = models.CharField(max_length=40, null=False)
    año = models.CharField(max_length=40, null=False)

    def __str__(self) -> str:
        return self.dia + " " + self.mes + " " + self.año

class ModeloDocumentacion(models.Model):

    documento = models.CharField(max_length=40, null=False)
    tipo = models.CharField(max_length=40, null=False)

    def __str__(self) -> str:
        return self.documento + " " + self.tipo

class ModeloPago(models.Model):

    metododepago = models.CharField(max_length=40, null=False)
    pagado = models.BooleanField(null=False)
    
    def __str__(self) -> str:
        return self.metododepago + " " + self.pagado
