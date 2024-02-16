from django.db import models

# Create your models here.
class Rubros(models.Model):
    clase = models.CharField(max_length=50)
    subClase = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.clase}"


class Areas(models.Model):
    area = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.area}"

class Personal(models.Model):
    nroLegajo = models.CharField(max_length=50)
    apellido_y_Nombre = models.CharField(max_length=50)
    agrupamiento = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nroLegajo}"


class Bienes(models.Model):
    dominio = models.CharField(max_length=50)
    subClase = models.CharField(max_length=50)
    anio = models.IntegerField()
    marcaModelo = models.CharField(max_length=50)
    nroChasis = models.CharField(max_length=50)
    nroMotor = models.CharField(max_length=50)
    accesorios = models.CharField(max_length=100)
    aseguradoraPoliza = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.dominio}"
