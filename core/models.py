from django.db import models

# Create your models here.
from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Actor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Convenio(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    pais = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    anio = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.provincia} - {self.pais} ({self.anio})"