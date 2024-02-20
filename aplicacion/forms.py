from django import forms

class AltaBienes(forms.Form):
    dominio = forms.CharField(max_length=50, required=True)
    subClase = forms.CharField(max_length=50, required=True)
    anio = forms.IntegerField(required=True)
    marcaModelo = forms.CharField(max_length=50, required=True)
    nroChasis = forms.CharField(max_length=50, required=True)
    nroMotor = forms.CharField(max_length=50, required=True)
    accesorios = forms.CharField(max_length=100, required=True)
    aseguradoraPoliza = forms.CharField(max_length=50, required=True)

class AltaRubros(forms.Form):
    clase = forms.CharField(max_length=50, required=True)
    subClase = forms.CharField(max_length=50, required=True)

class AltaPersonal(forms.Form):
    nroLegajo = forms.CharField(max_length=50, required=True)
    apellido_y_Nombre = forms.CharField(max_length=50, required=True)
    agrupamiento = forms.CharField(max_length=50, required=True)
    cargo = forms.CharField(max_length=50, required=True)
    destino = forms.CharField(max_length=100, required=True)

class AltaAreas(forms.Form):
    area = forms.CharField(max_length=50, required=True)
    destino = forms.CharField(max_length=50, required=True)
    responsable = forms.CharField(max_length=50, required=True)
