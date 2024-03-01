from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.urls import reverse_lazy
from aplicacion import *
from .models import *
from .forms import *

#from django.views.generic import ListView
#from django.views.generic import CreateView
#from django.views.generic import UpdateView
#from django.views.generic import DeleteView

#from django.contrib.auth.forms      import AuthenticationForm
#from django.contrib.auth            import authenticate, login, logout
#from django.contrib.auth.mixins     import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required

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

# Alta de Rubros

def altaRubros(request):
    contexto = {'rubros': Rubros.objects.all()}
    if request.method == "POST":
        nuevoAlta = AltaRubros(request.POST)
        if nuevoAlta.is_valid():
            rubro_clase = nuevoAlta.cleaned_data.get('clase')
            rubro_subclase = nuevoAlta.cleaned_data.get('subClase')
            rubros = Rubros(clase=rubro_clase, subClase=rubro_subclase)
            rubros.save()
            return redirect(reverse_lazy('rubros'))
    else:   
        nuevoAlta = AltaRubros()
    return render (request, "aplicacion/alta_rubro.html", {"form": nuevoAlta})

#Buscar Rubros

def buscar(request):
    return render(request, 'aplicacion/buscar.html')

def buscarRubros(request):
    if request.GET["buscar"]:
        dato = request.GET["buscar"]
        rubros = Rubros.objects.filter(clase__icontains=dato)
        contexto ={"rubros": rubros}
        return render(request, "aplicacion/rubros.html", contexto)
    return HttpResponse("No se Ingresaron Datos a Buscar")

#Editar Rubros

def editarRubro(request, id_rubro):
    rubro = Rubros.objects.get(id=id_rubro)
    if request.method == "POST":
        nuevoAlta = AltaRubros(request.POST)
        if nuevoAlta.is_valid():
            rubro.clase = nuevoAlta.cleaned_data.get('clase')
            rubro.subClase = nuevoAlta.cleaned_data.get('subClase')
            rubro.save()
            return redirect(reverse_lazy('rubros'))   
    else:
        nuevoAlta = AltaRubros(initial={
            'clase': rubro.clase,
            'subClase': rubro.subClase,
        })
    return render(request, "aplicacion/alta_rubro.html", {'form': nuevoAlta})

#Eliminar Rubros

def eliminarRubros(request, id_rubro):
    rubros = Rubros.objects.get(id=id_rubro)
    rubros.delete()
    return redirect(reverse_lazy('rubros'))



#_________________________--------__________________________________

#AREAS

def areas(request):
    contexto = {'areas': Areas.objects.all()}
    return render (request, "aplicacion/areas.html", contexto)

def altaArea(request):
    nuevoAlta = AltaAreas()
    return render (request, "aplicacion/alta_area.html", {"form": nuevoAlta})

#Alta Areas

def altaAreas(request):
    contexto = {'areas': Areas.objects.all()}
    if request.method == "POST":
        nuevoAlta = AltaAreas(request.POST)
        if nuevoAlta.is_valid():
            area_area = nuevoAlta.cleaned_data.get('area')
            area_destino = nuevoAlta.cleaned_data.get('destino')
            area_responsable = nuevoAlta.cleaned_data.get('responsable')
            areas = Areas(area=area_area, destino=area_destino, responsable=area_responsable)
            areas.save()
            return redirect(reverse_lazy('areas'))
    else:   
        nuevoAlta = AltaAreas()
    return render (request, "aplicacion/alta_area.html", {"form": nuevoAlta})

#Editar Areas

def editarArea(request, id_area):
    area = Areas.objects.get(id=id_area)
    if request.method == "POST":
        nuevoAlta = AltaAreas(request.POST)
        if nuevoAlta.is_valid():
            area.area = nuevoAlta.cleaned_data.get('area')
            area.destino = nuevoAlta.cleaned_data.get('destino')
            area.responsable = nuevoAlta.cleaned_data.get('responsable')
            area.save()
            return redirect(reverse_lazy('areas'))   
    else:
        nuevoAlta = AltaAreas(initial={
            'area': area.area,
            'destino': area.destino,
            'responsable': area.responsable,
        })
    return render(request, "aplicacion/alta_area.html", {'form': nuevoAlta})

#Eliminar Areas

def eliminarArea(request, id_area):
    area = Areas.objects.get(id=id_area)
    area.delete()
    return redirect(reverse_lazy('areas'))

#_________________________--------__________________________________

#PERSONAL

def personal(request):
    contexto = {'personal': Personal.objects.all()}
    return render (request, "aplicacion/personal.html", contexto)


def altaPersonal(request):
    nuevoAlta = AltaPersonal()
    return render (request, "aplicacion/alta_personal.html", {"form": nuevoAlta})

#Alta Personal

def altaPersonal(request):
    contexto = {'personal': Personal.objects.all()}
    if request.method == "POST":
        nuevoAlta = AltaPersonal(request.POST)
        if nuevoAlta.is_valid():
            persona_nrolegajo = nuevoAlta.cleaned_data.get('nroLegajo')
            persona_apellido_y_nombre = nuevoAlta.cleaned_data.get('apellido_y_Nombre')
            persona_agrupamiento = nuevoAlta.cleaned_data.get('agrupamiento')
            persona_cargo = nuevoAlta.cleaned_data.get('cargo')
            persona_destino = nuevoAlta.cleaned_data.get('destino')
            personal = Personal(nroLegajo=persona_nrolegajo, apellido_y_Nombre=persona_apellido_y_nombre,
                                agrupamiento=persona_agrupamiento, cargo=persona_cargo, destino=persona_destino)
            personal.save() 
            return redirect(reverse_lazy('personal'))
    else:   
        nuevoAlta = AltaPersonal()
    return render (request, "aplicacion/alta_bienes.html", {"form": nuevoAlta})

#Editar Personal

def editarPersonal(request, id_personal):
    personal = Personal.objects.get(id=id_personal)
    if request.method == "POST":
        nuevoAlta = AltaPersonal(request.POST)
        if nuevoAlta.is_valid():
            personal.nroLegajo = nuevoAlta.cleaned_data.get('nroLegajo')
            personal.apellido_y_Nombre = nuevoAlta.cleaned_data.get('apellido_y_Nombre')
            personal.agrupamiento = nuevoAlta.cleaned_data.get('agrupamiento')
            personal.cargo = nuevoAlta.cleaned_data.get('cargo')
            personal.destino = nuevoAlta.cleaned_data.get('destino')
            personal.save()
            return redirect(reverse_lazy('personal'))   
    else:
        nuevoAlta = AltaPersonal(initial={
            'nroLegajo': personal.nroLegajo,
            'apellido_y_Nombre': personal.apellido_y_Nombre,
            'agrupamiento': personal.agrupamiento,
            'cargo': personal.cargo,
            'destino': personal.destino,
        })
    return render(request, "aplicacion/alta_personal.html", {'form': nuevoAlta})

#Eliminar Personal

def eliminarPersonal(request, id_personal):
    personal = Personal.objects.get(id=id_personal)
    personal.delete()
    return redirect(reverse_lazy('personal'))

#_________________________--------__________________________________


#BIENES

def bienes(request):
    contexto = {'bienes': Bienes.objects.all()} 
    return render (request, "aplicacion/bienes.html", contexto)

#Alta Bienes
def altaBienes(request):
    contexto = {'bienes': Bienes.objects.all()}
    if request.method == "POST":
        nuevoAlta = AltaBienes(request.POST)
        if nuevoAlta.is_valid():
            bienes_subclase = nuevoAlta.cleaned_data.get('subClase')
            bienes_anio = nuevoAlta.cleaned_data.get('anio')
            bienes_dominio = nuevoAlta.cleaned_data.get('dominio')
            bienes_marcamodelo = nuevoAlta.cleaned_data.get('marcaModelo')
            bienes_nrochasis = nuevoAlta.cleaned_data.get('nroChasis')
            bienes_nromotor = nuevoAlta.cleaned_data.get('nroMotor')
            bienes_accesorios = nuevoAlta.cleaned_data.get('accesorios')
            bienes_aseguradorapoliza = nuevoAlta.cleaned_data.get('aseguradoraPoliza')
            bienes = Bienes(dominio=bienes_dominio, subClase=bienes_subclase, anio=bienes_anio, marcaModelo=bienes_marcamodelo,
                            nroChasis=bienes_nrochasis, nroMotor=bienes_nromotor, accesorios=bienes_accesorios, aseguradoraPoliza=bienes_aseguradorapoliza)
            bienes.save()
            return redirect(reverse_lazy('bienes'))
    else:   
        nuevoAlta = AltaBienes()
    return render (request, "aplicacion/alta_bienes.html", {"form": nuevoAlta})

#@login_required
def editarBienes(request, id_bienes):
    bienes = Bienes.objects.get(id=id_bienes)
    if request.method == "POST":
        nuevoAlta = AltaBienes(request.POST)
        if nuevoAlta.is_valid():
            bienes.dominio = nuevoAlta.cleaned_data.get('dominio')
            bienes.subClase = nuevoAlta.cleaned_data.get('subClase')
            bienes.anio = nuevoAlta.cleaned_data.get('anio')
            bienes.marcaModelo = nuevoAlta.cleaned_data.get('marcaModelo')
            bienes.nroChasis = nuevoAlta.cleaned_data.get('nroChasis')
            bienes.nroMotor = nuevoAlta.cleaned_data.get('nroMotor')
            bienes.accesorios = nuevoAlta.cleaned_data.get('accesorios')
            bienes.aseguradoraPoliza = nuevoAlta.cleaned_data.get('aseguradoraPoliza')
            bienes.save()
            return redirect(reverse_lazy('bienes'))   
        else:
            nuevoAlta = AltaBienes(initial={
            'dominio': bienes.dominio,
            'subClase': bienes.subClase,
            'anio': bienes.anio,
            'marcaModelo': bienes.marcaModelo,
            'nroChasis': bienes.nroChasis,
            'nroMotor': bienes.nroMotor,
            'accesorios': bienes.accesorios,
            'aseguradoraPoliza': bienes.aseguradoraPoliza,
        })
    return render(request, "aplicacion/alta_bienes.html", {'form': nuevoAlta})

#@login_required
def eliminarBienes(request, id_bienes):
    bienes = Bienes.objects.get(id=id_bienes)
    bienes.delete()
    return redirect(reverse_lazy('bienes'))

#_________________________--------__________________________________
#BIENES (usando clases basados en vista)

#class BienesList(ListView):
    #model = Bienes

#class BienesCreate(CreateView):
    #model = Bienes
    #fields = ['dominio', 'subClase', 'anio', 'marcaModelo', 'nroChasis', 'nroMotor', 'accesorios','aseguradoraPoliza']
    #success_url = reverse_lazy('bienes')

#class BienesUpdate(UpdateView):
    #model = Bienes
    #fields = ['dominio', 'subClase', 'anio', 'marcaModelo', 'nroChasis', 'nroMotor', 'accesorios','aseguradoraPoliza']
    #success_url = reverse_lazy('bienes')

#class BienesDelete(DeleteView):
    #model = Bienes
    #success_url = reverse_lazy('bienes')
