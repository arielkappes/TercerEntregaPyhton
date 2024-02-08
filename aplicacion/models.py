from django.db import models

# Create your models here.
class Rubros(models.Model):
    Clase = models.CharField(max_length=50)
    SubClase = models.CharField(max_length=50)


class Areas(models.Model):
    Area = models.CharField(max_length=50)
    Destino = models.CharField(max_length=50)
    Responsable = models.CharField(max_length=50)

class Personal(models.Model):
    NroLegajo = models.CharField(max_length=50)
    Apellido_y_Nombre = models.CharField(max_length=50)
    Agrupamiento = models.CharField(max_length=50)
    Cargo = models.CharField(max_length=50)
    Destino = models.CharField(max_length=50)


class Bienes(models.Model):
    Dominio = models.CharField(max_length=50)
    SubClase = models.CharField(max_length=50)
    Anio = models.DateField(max_length=50)
    MarcaModelo = models.CharField(max_length=50)
    NroChasis = models.CharField(max_length=50)
    NroMotor = models.CharField(max_length=50)
    Accesorios = models.CharField(max_length=100)
    AeguradoraPoliza = models.CharField(max_length=50)
