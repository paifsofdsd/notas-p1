from django.urls import path

from .views import calcularAB1, calcularAB2, importFinal, importLista, importProva, importReav, index, notasAcumuladas, resolution, importation, searchNotaGeral, searchNotaIndividual

urlpatterns = [
    path('', index, name='index'),
    path('resolution/', resolution, name='resolution'),
    path('importation/', importation, name='importation'),
    path('importp1/', importProva, name='importp1'),
    path('importp2/', importProva, name='importp2'),
    path('importp3/', importProva, name='importp3'),
    path('importp4/', importProva, name='importp4'),
    path('importl1/', importLista, name='importl1'),
    path('importl2/', importLista, name='importl2'),
    path('importl3/', importLista, name='importl3'),
    path('importl4/', importLista, name='importl4'),
    path('importl5/', importLista, name='importl5'),
    path('importl6/', importLista, name='importl6'),
    path('importl7/', importLista, name='importl7'),
    path('importl8/', importLista, name='importl8'),
    path('importreav/', importReav, name='importreav'),
    path('importfinal/', importFinal, name='importfinal'),
    path('calcularab1/', calcularAB1, name='calcularab1'),
    path('calcularab2/', calcularAB2, name='calcularab2'),
    path('notas/', notasAcumuladas, name='notas'),
    path('resolution/search/', searchNotaIndividual, name='searchindividual'),
    path('notas/search/', searchNotaGeral, name='searchgeral'),
]