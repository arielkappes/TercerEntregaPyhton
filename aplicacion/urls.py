from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    #RUBROS
    path('rubros/', rubros, name='rubros'),
    #
    path('alta_rubro/', altaRubros, name= "AltaRubros"),
    
    #_________________-------___________________________
    
    #AREAS
    path('areas/', areas, name='areas'),
    #
    path('alta_area/', AltaAreas, name= "AltaAreas"),
    #_________________-------___________________________
    

    #PERSONAL
    path('personal/', personal, name='personal'),
    #
    path('alta_personal/', altaPersonal, name= "AltaPersonal"),
    #_________________-------___________________________
    
    #BIENES
    path('bienes/', bienes, name='bienes'),
    #
    path('alta_bienes/', AltaBienes, name= "AltaBienes"),
    #_________________-------___________________________
]