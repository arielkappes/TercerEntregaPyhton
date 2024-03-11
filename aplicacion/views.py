from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.urls import reverse_lazy
from aplicacion import *
from .models import *
from .forms import *
from django.http import HttpResponse
import openpyxl
from io import BytesIO









from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render (request, "aplicacion/home.html")

#RUBROS
@login_required
def rubros(request):
    contexto = {'rubro': Rubros.objects.all()}
    return render (request, "aplicacion/rubros.html", contexto)
@login_required
def altaRubros(request):
    nuevoAlta = AltaRubros()
    return render (request, "aplicacion/alta_rubro.html", {"form": nuevoAlta})

# Alta de Rubros
#@login_required
#def altaRubros(request):
    #contexto = {'rubros': Rubros.objects.all()}
    #if request.method == "POST":
        #nuevoAlta = AltaRubros(request.POST)
        #if nuevoAlta.is_valid():
            #rubro_clase = nuevoAlta.cleaned_data.get('clase')
            #rubro_subclase = nuevoAlta.cleaned_data.get('subClase')
            #rubros = Rubros(clase=rubro_clase, subClase=rubro_subclase)
            #rubros.save()
            #return redirect(reverse_lazy('rubros'))
    #else:   
        #n#uevoAlta = AltaRubros()
    #return render (request, "aplicacion/alta_rubro.html", {"form": nuevoAlta})

#Buscar Rubros
#@login_required
#def buscar(request):
    #return render(request, 'aplicacion/buscar.html')
#@login_required
#def buscarRubros(request):
    #if request.GET["buscar"]:
        #dato = request.GET["buscar"]
        #rubros = Rubros.objects.filter(clase__icontains=dato)
        #contexto ={"rubros": rubros}
        #return render(request, "aplicacion/rubros.html", contexto)
    #return HttpResponse("No se Ingresaron Datos a Buscar")

#Editar Rubros
#@login_required
#def editarRubro(request, id_rubro):
    #rubro = Rubros.objects.get(id=id_rubro)
    #if request.method == "POST":
        #nuevoAlta = AltaRubros(request.POST)
        #if nuevoAlta.is_valid():
            #rubro.clase = nuevoAlta.cleaned_data.get('clase')
            #rubro.subClase = nuevoAlta.cleaned_data.get('subClase')
            #rubro.save()
            #return redirect(reverse_lazy('rubros'))   
    #else:
        #nuevoAlta = AltaRubros(initial={
            #'clase': rubro.clase,
            #'subClase': rubro.subClase,
        #})
    #return render(request, "aplicacion/alta_rubro.html", {'form': nuevoAlta})

#Eliminar Rubros
#@login_required
#def eliminarRubros(request, id_rubro):
    #rubros = Rubros.objects.get(id=id_rubro)
    #rubros.delete()
    #return redirect(reverse_lazy('rubros'))



#_________________________--------__________________________________

#AREAS
#@login_required
#def areas(request):
    #contexto = {'areas': Areas.objects.all()}
    #return render (request, "aplicacion/areas.html", contexto)

#@login_required
#def altaArea(request):
    #nuevoAlta = AltaAreas()
    #return render (request, "aplicacion/alta_area.html", {"form": nuevoAlta})

#Alta Areas

#def altaAreas(request):
    #contexto = {'areas': Areas.objects.all()}
    #if request.method == "POST":
        #nuevoAlta = AltaAreas(request.POST)
        #if nuevoAlta.is_valid():
            #area_area = nuevoAlta.cleaned_data.get('area')
            #area_destino = nuevoAlta.cleaned_data.get('destino')
            #area_responsable = nuevoAlta.cleaned_data.get('responsable')
            #areas = Areas(area=area_area, destino=area_destino, responsable=area_responsable)
            #areas.save()
            #return redirect(reverse_lazy('areas'))
    #else:   
        #nuevoAlta = AltaAreas()
    #return render (request, "aplicacion/alta_area.html", {"form": nuevoAlta})

#Editar Areas

#def editarArea(request, id_area):
    #area = Areas.objects.get(id=id_area)
    #if request.method == "POST":
        #nuevoAlta = AltaAreas(request.POST)
        #if nuevoAlta.is_valid():
        #area.area = nuevoAlta.cleaned_data.get('area')
        #area.destino = nuevoAlta.cleaned_data.get('destino')
        #area.responsable = nuevoAlta.cleaned_data.get('responsable')
        #area.save()
        #return redirect(reverse_lazy('areas'))   
    #else:
        #nuevoAlta = AltaAreas(initial={
            #'area': area.area,
            #'destino': area.destino,
            #'responsable': area.responsable,
        #})
    #return render(request, "aplicacion/alta_area.html", {'form': nuevoAlta})

#Eliminar Areas

#def eliminarArea(request, id_area):
    #area = Areas.objects.get(id=id_area)
    #area.delete()
    #return redirect(reverse_lazy('areas'))

#_________________________--------__________________________________

#PERSONAL
#@login_required
#def personal(request):
    #contexto = {'personal': Personal.objects.all()}
    r#eturn render (request, "aplicacion/personal.html", contexto)

#@login_required
#def altaPersonal(request):
    #nuevoAlta = AltaPersonal()
    r#eturn render (request, "aplicacion/alta_personal.html", {"form": nuevoAlta})

#Alta Personal
#@login_required
#def altaPersonal(request):
    #contexto = {'personal': Personal.objects.all()}
    #if request.method == "POST":
        #nuevoAlta = AltaPersonal(request.POST)
        #if nuevoAlta.is_valid():
            #persona_nrolegajo = nuevoAlta.cleaned_data.get('nroLegajo')
            #persona_apellido_y_nombre = nuevoAlta.cleaned_data.get('apellido_y_Nombre')
            #persona_agrupamiento = nuevoAlta.cleaned_data.get('agrupamiento')
            #persona_cargo = nuevoAlta.cleaned_data.get('cargo')
            #ersona_destino = nuevoAlta.cleaned_data.get('destino')
            #personal = Personal(nroLegajo=persona_nrolegajo, apellido_y_Nombre=persona_apellido_y_nombre,
                                #agrupamiento=persona_agrupamiento, cargo=persona_cargo, destino=persona_destino)
            #personal.save() 
            #return redirect(reverse_lazy('personal'))
    #else:   
        #nuevoAlta = AltaPersonal()
    #return render (request, "aplicacion/alta_PERSONAL.html", {"form": nuevoAlta})

#Editar Personal
#@login_required
#def editarPersonal(request, id_personal):
    #personal = Personal.objects.get(id=id_personal)
    #if request.method == "POST":
        #nuevoAlta = AltaPersonal(request.POST)
        #if nuevoAlta.is_valid():
            #personal.nroLegajo = nuevoAlta.cleaned_data.get('nroLegajo')
            #personal.apellido_y_Nombre = nuevoAlta.cleaned_data.get('apellido_y_Nombre')
            #personal.agrupamiento = nuevoAlta.cleaned_data.get('agrupamiento')
            #personal.cargo = nuevoAlta.cleaned_data.get('cargo')
            #personal.destino = nuevoAlta.cleaned_data.get('destino')
            #personal.save()
            #return redirect(reverse_lazy('personal'))   
    #else:
        #nuevoAlta = AltaPersonal(initial={
            #'nroLegajo': personal.nroLegajo,
            #'apellido_y_Nombre': personal.apellido_y_Nombre,
            #'agrupamiento': personal.agrupamiento,
            #'cargo': personal.cargo,
            #'destino': personal.destino,
        #})
    #return render(request, "aplicacion/alta_personal.html", {'form': nuevoAlta})

#Eliminar Personal
#@login_required
#def eliminarPersonal(request, id_personal):
    #personal = Personal.objects.get(id=id_personal)
    #personal.delete()
    #return redirect(reverse_lazy('personal'))
    


#_________________________--------_____________S_____________________


#BIENES (usando funciones -- solo de muestra --)

#def bienes(request):
    #contexto = {'bienes': Bienes.objects.all()} 
    #return render (request, "aplicacion/bienes.html", contexto)

#Alta Bienes 
#def altaBienes(request):
    #contexto = {'bienes': Bienes.objects.all()}
    #if request.method == "POST":
        #nuevoAlta = AltaBienes(request.POST)
        #if nuevoAlta.is_valid():
            #bienes_subclase = nuevoAlta.cleaned_data.get('subClase')
            #bienes_anio = nuevoAlta.cleaned_data.get('anio')
            #bienes_dominio = nuevoAlta.cleaned_data.get('dominio')
            #bienes_marcamodelo = nuevoAlta.cleaned_data.get('marcaModelo')
            #bienes_nrochasis = nuevoAlta.cleaned_data.get('nroChasis')
            #bienes_nromotor = nuevoAlta.cleaned_data.get('nroMotor')
            #bienes_accesorios = nuevoAlta.cleaned_data.get('accesorios')
            #bienes_aseguradorapoliza = nuevoAlta.cleaned_data.get('aseguradoraPoliza')
            #bienes = Bienes(dominio=bienes_dominio, subClase=bienes_subclase, anio=bienes_anio, marcaModelo=bienes_marcamodelo,
                            #nroChasis=bienes_nrochasis, nroMotor=bienes_nromotor, accesorios=bienes_accesorios, aseguradoraPoliza=bienes_aseguradorapoliza)
            #bienes.save()
            #return redirect(reverse_lazy('bienes'))
        #else:   
            #nuevoAlta = AltaBienes()
    #return render (request, "aplicacion/alta_bienes.html", {"form": nuevoAlta})


#d#ef editarBienes(request, id_bienes):
    #bienes = Bienes.objects.get(id=id_bienes)
    #if request.method == "POST":
        #nuevoAlta = AltaBienes(request.POST)
        #if nuevoAlta.is_valid():
            #bienes.dominio = nuevoAlta.cleaned_data.get('dominio')
            #bienes.subClase = nuevoAlta.cleaned_data.get('subClase')
            #bienes.anio = nuevoAlta.cleaned_data.get('anio')
            #bienes.marcaModelo = nuevoAlta.cleaned_data.get('marcaModelo')
            #bienes.nroChasis = nuevoAlta.cleaned_data.get('nroChasis')
            #bienes.nroMotor = nuevoAlta.cleaned_data.get('nroMotor')
            #bienes.accesorios = nuevoAlta.cleaned_data.get('accesorios')
            #bienes.aseguradoraPoliza = nuevoAlta.cleaned_data.get('aseguradoraPoliza')
            #bienes.save()
            #return redirect(reverse_lazy('bienes'))   
        #else:
            #nuevoAlta = AltaBienes(initial={
            #'dominio': bienes.dominio,
            #'subClase': bienes.subClase,
            #'anio': bienes.anio,
            #'marcaModelo': bienes.marcaModelo,
            #'nroChasis': bienes.nroChasis,
            #'nroMotor': bienes.nroMotor,
            #'accesorios': bienes.accesorios,
            #'aseguradoraPoliza': bienes.aseguradoraPoliza,
            #})
    #return render(request, "aplicacion/alta_bienes.html", {'form': nuevoAlta})


#def eliminarBienes(request, id_bienes):
    #bienes = Bienes.objects.get(id=id_bienes)
    #bienes.delete()
    #return redirect(reverse_lazy('bienes'))

#_________________________--------__________________________________
#BIENES (usando clases basados en vista)


class BienesList(LoginRequiredMixin, ListView):
    model = Bienes
    

class BienesCreate(LoginRequiredMixin, CreateView):
    model = Bienes
    fields = ['dominio', 'subClase', 'anio', 'marcaModelo', 'nroChasis', 'nroMotor', 'accesorios','aseguradoraPoliza']
    success_url = reverse_lazy('bienes')
    

class BienesUpdate(LoginRequiredMixin, UpdateView):
    model = Bienes
    fields = ['dominio', 'subClase', 'anio', 'marcaModelo', 'nroChasis', 'nroMotor', 'accesorios','aseguradoraPoliza']
    success_url = reverse_lazy('bienes')
    

class BienesDelete(LoginRequiredMixin, DeleteView):
    model = Bienes
    success_url = reverse_lazy('bienes')

#_________________________--------__________________________________

#AREAS (usando clases basados en vista)


class AreasList(LoginRequiredMixin, ListView):
    model = Areas
    

class AreasCreate(LoginRequiredMixin, CreateView):
    model = Areas
    fields = ['area', 'destino', 'responsable']
    success_url = reverse_lazy('areas')
    

class AreasUpdate(LoginRequiredMixin, UpdateView):
    model = Areas
    fields = ['area', 'destino', 'responsable']
    success_url = reverse_lazy('areas')

class AreasDelete(LoginRequiredMixin, DeleteView):
    model = Areas
    success_url = reverse_lazy('areas')

#_________________________--------__________________________________

class PersonalList(LoginRequiredMixin, ListView):
    model = Personal
    

class PersonalCreate(LoginRequiredMixin, CreateView):
    model = Personal
    fields = ['nroLegajo', 'apellido_y_Nombre', 'agrupamiento', 'cargo', 'destino']
    success_url = reverse_lazy('personal')
    

class PersonalUpdate(LoginRequiredMixin, UpdateView):
    model = Personal
    fields = ['nroLegajo', 'apellido_y_Nombre', 'agrupamiento', 'cargo', 'destino']
    success_url = reverse_lazy('personal')
    

class PersonalDelete(LoginRequiredMixin, DeleteView):
    model = Personal
    success_url = reverse_lazy('personal')
    #-----------------------

class RubrosList(LoginRequiredMixin, ListView):
    model = Rubros
    

class RubrosCreate(LoginRequiredMixin, CreateView):
    model = Rubros
    fields = ['clase', 'subClase']
    success_url = reverse_lazy('rubros')
    

class RubrosUpdate(LoginRequiredMixin, UpdateView):
    model = Rubros
    fields = ['clase', 'subClase']
    success_url = reverse_lazy('rubros')
    

class RubrosDelete(LoginRequiredMixin, DeleteView):
    model = Rubros
    success_url = reverse_lazy('rubros')



#------------------------------
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            print("usuario valido")
            login(request, user)
            #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________


            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
        
    nuevoAlta = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": nuevoAlta })    

@login_required
def custom_logout(request):
    logout(request)
    return redirect(reverse_lazy('home'))



def register(request):
    if request.method == "POST":
        nuevoAlta = RegistroForm(request.POST)
        if nuevoAlta.is_valid():
            usuario = nuevoAlta.cleaned_data.get("username")
            nuevoAlta.save()
            return redirect(reverse_lazy('home'))

    else:    
        nuevoAlta = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": nuevoAlta })  

#__________________________ Editar perfil de usuario

def editarPerfil(request):
    usuario = request.user

    form = UserEditForm(instance=usuario) 

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")

    return render(request, "aplicacion/editarPerfil.html", {"form": form }) 

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # __________________________________
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___________ Hago una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/home.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form }) 

#-----------__________-----------------------

def descargar_excel(request):
    bienes = Bienes.objects.all()  

    # Crear un libro de trabajo de Excel y una hoja de cálculo
    libro_trabajo = openpyxl.Workbook()
    hoja = libro_trabajo.active
    hoja.title = "Bienes"

    hoja.append(['dominio', 'subClase', 'anio', 'marcaModelo', 'nroChasis', 'nroMotor', 'accesorios','aseguradoraPoliza'])
    
    for b in bienes:
        hoja.append([b.dominio, b.subClase, b.anio, b.marcaModelo, b.nroChasis, b.nroMotor, b.accesorios, b.aseguradoraPoliza])

    output = BytesIO()
    libro_trabajo.save(output)
    output.seek(0)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Bienes.xlsx'
    response.write(output.getvalue())
    return response


def sobre_mi(request):
    return render(request, 'aplicacion/sobre_mi.html')