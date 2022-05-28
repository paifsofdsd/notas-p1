from django.urls import path

from .views import importLista1, importLista2, importLista3, importLista4, importLista5, importLista6, importLista7, importLista8, importProva2, importProva3, importProva4, index, resolution, importation, importProva1

urlpatterns = [
    path('', index, name='index'),
    path('resolution', resolution, name='resolution'),
    path('importation', importation, name='importation'),
    path('importp1', importProva1, name='importp1'),
    path('importp2', importProva2, name='importp2'),
    path('importp3', importProva3, name='importp3'),
    path('importp4', importProva4, name='importp4'),
    path('importl1', importLista1, name='importl1'),
    path('importl2', importLista2, name='importl2'),
    path('importl3', importLista3, name='importl3'),
    path('importl4', importLista4, name='importl4'),
    path('importl5', importLista5, name='importl5'),
    path('importl6', importLista6, name='importl6'),
    path('importl7', importLista7, name='importl7'),
    path('importl8', importLista8, name='importl8'),
]