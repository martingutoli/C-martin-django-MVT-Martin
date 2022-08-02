from django.db import models
from datetime import  datetime
# Create your models here.
class Datos_familia(models.Model):

    nombre = models.CharField(max_length=40)

    fecha_nac = models.DateField()

    edad = models.IntegerField()

    relacion = models.CharField(max_length=40)

    