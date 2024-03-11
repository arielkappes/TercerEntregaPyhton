from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', home, name='home'),
    
    #RUBROS
    #path('rubros/', rubros, name='rubros'),
    #
    #path('alta_rubro/', altaRubros, name= "AltaRubros"),
    #
    #path('buscar/', buscar, name= "buscar"),
    #path('buscarRubros/', buscarRubros, name= "buscarRubros"),
    #
    #path('editar_rubro/<id_rubro>/', editarRubro, name= "EditarRubros"),
    #path('eliminar_rubro/<id_rubro>/', eliminarRubros, name= "EliminarRubro"),
    
    path('rubros/', RubrosList.as_view(), name= "rubros"),
    path('rubros_create/', RubrosCreate.as_view(), name="rubros_create"),
    path('rubros_update/<int:pk>/', RubrosUpdate.as_view(), name="rubros_update"),
    path('rubros_delete/<int:pk>/', RubrosDelete.as_view(), name="rubros_delete"),
    #_________________-------___________________________
    
    #AREAS
    #path('areas/', areas, name='areas'),
    #
    #path('alta_area/', AltaAreas, name= "AltaAreas"),
    
    # AREAS ( con Clases Basados en vistas )
    path('areas/', AreasList.as_view(), name= "areas"),
    path('areas_create/', AreasCreate.as_view(), name="areas_create"),
    path('areas_update/<int:pk>/', AreasUpdate.as_view(), name="areas_update"),
    path('areas_delete/<int:pk>/', AreasDelete.as_view(), name="areas_delete"),
    #_________________-------___________________________
    

    #PERSONAL
    #path('personal/', personal, name='personal'),
    #
    #path('alta_personal/', altaPersonal, name= "AltaPersonal"),
    #
    #path('editar_personal/<id_personal>/', editarPersonal, name= "EditarPersonal"),
    #path('eliminar_personal/<id_personal>/', eliminarPersonal, name= "EliminarPersonal"),
    path('personal/', PersonalList.as_view(), name= "personal"),
    path('personal_create/', PersonalCreate.as_view(), name="personal_create"),
    path('personal_update/<int:pk>/', PersonalUpdate.as_view(), name="personal_update"),
    path('personal_delete/<int:pk>/', PersonalDelete.as_view(), name="personal_delete"),
    
    #_________________-------___________________________
    
    
    # BIENES ( con Clases Basados en vistas )
    path('bienes/', BienesList.as_view(), name= "bienes"),
    path('bienes_create/', BienesCreate.as_view(), name="bienes_create"),
    path('bienes_update/<int:pk>/', BienesUpdate.as_view(), name="bienes_update"),
    path('bienes_delete/<int:pk>/', BienesDelete.as_view(), name="bienes_delete"),
    #_________________-------___________________________
    
#LOGIN´s
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', custom_logout, name="logout"),
    
#AVATAR´s
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
#Descarga
    path('descargar-excel/', views.descargar_excel, name='descargar_excel'),
    
#link
    path('Sobre_mi/', views.sobre_mi, name='sobre_mi')
    
]
