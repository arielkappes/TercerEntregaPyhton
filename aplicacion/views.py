from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime, random
from aplicacion import *
from .models import *

# Create your views here.
def home(request):
    return render (request, "aplicacion/home.html")

def rubros(request):
    return render (request, "aplicacion/rubros.html")
    
#AREAS
def areas(request):
    contexto = {'Areas': Areas.objects.all()}
    return render (request, "aplicacion/areas.html", contexto)

def personal(request):
    return render (request, "aplicacion/personal.html")

#BIENES
def bienes(request): 
    return render (request, "aplicacion/bienes.html")

def bienesForm(request):
    return render (request, "aplicacion/bienesForm.html")