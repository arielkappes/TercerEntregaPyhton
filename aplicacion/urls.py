from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    path('rubros/', rubros, name='rubros'),
    #AREAS
    path('areas/', areas, name='areas'),

    
    path('personal/', personal, name='personal'),
    
    path('bienes/', bienes, name='bienes'),
    #
    path('bienesForm/', bienesForm, name='bienesForm'),
]