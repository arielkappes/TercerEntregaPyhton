from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)