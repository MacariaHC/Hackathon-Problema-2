from django.db import models

# Create your models here.

class Aspirantes(models.Model):
    ficha = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=200)
    ingles = models.CharField(max_length=50)
    promedio = models.PositiveSmallIntegerField()
    carrera = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    
    


