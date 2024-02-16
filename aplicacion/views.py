from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime, random
from aplicacion import *
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render (request, "aplicacion/home.html")

#RUBROS
def rubros(request):
    contexto = {'rubro': Rubros.objects.all()}
    return render (request, "aplicacion/rubros.html", contexto)

def altaRubros(request):
    nuevoAlta = AltaRubros()
    return render (request, "aplicacion/alta_rubro.html", {"form": nuevoAlta})


#AREAS
def areas(request):
    contexto = {'areas': Areas.objects.all()}
    return render (request, "aplicacion/areas.html", contexto)

def altaArea(request):
    nuevoAlta = AltaAreas()
    return render (request, "aplicacion/alta_area.html", {"form": nuevoAlta})


#PERSONAL
def personal(request):
    contexto = {'personal': Personal.objects.all()}
    return render (request, "aplicacion/personal.html", contexto)

def altaPersonal(request):
    nuevoAlta = AltaPersonal()
    return render (request, "aplicacion/alta_personal.html", {"form": nuevoAlta})

#BIENES
def bienes(request):
    contexto = {'bienes': Bienes.objects.all()} 
    return render (request, "aplicacion/bienes.html", contexto)


def altaBienes(request):
    if request.method == "POST":
        nuevoAlta = AltaBienes(request.POST)
        if nuevoAlta.is_valid():
            bien_dominio = nuevoAlta.cleaned_data.get('dominio')
            bien_subclase = nuevoAlta.cleaned_data.get('subClase')
            bien_anio = nuevoAlta.cleaned_data.get('anio')
            bien_marcamodelo = nuevoAlta.cleaned_data.get('marcaModelo')
            bien_nrochasis = nuevoAlta.cleaned_data.get('nroChasis')
            bien_nromotor = nuevoAlta.cleaned_data.get('nroMotor')
            bien_accesorios = nuevoAlta.cleaned_data.get('accesorios')
            bien_aseguradorapoliza = nuevoAlta.cleaned_data.get('aseguradoraPoliza')
            bienes = Bienes(dominio=bien_dominio, subClase=bien_subclase, anio=bien_anio, marcaModelo=bien_marcamodelo,
                            nroChasis=bien_nrochasis, nroMotor=bien_nromotor, accesorios=bien_accesorios, aseguradoraPoliza=bien_aseguradorapoliza)
            bienes.save()
            return render(request, "aplicacion/bienes.html")
    else:   
        nuevoAlta = AltaBienes()
    return render (request, "aplicacion/alta_bienes.html", {"form": nuevoAlta})