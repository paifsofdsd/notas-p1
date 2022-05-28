from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno, NotaAluno
from django.contrib import messages
import pandas as pd
from decimal import *


def index(request):
    return render(request, 'nota/index.html')

def resolution(request):

    data = {}
    colunas = ('Nome', 'Turma', 'Prova 1', 
    'Lista 1', 'Lista 2', 'Prova 2', 'Lista 3',
    'Lista 4', 'Prova 3', 'Lista 5', 'Lista 6',
    'Prova 4', 'Lista 7', 'Lista 8')

    data['alunos'] = Aluno.objects.all()
    data['colunas'] = colunas

    return render(request, 'nota/resolution.html', data)

def importation(request):
    return render(request, 'nota/import.html')

def tratando_nota(new_aluno):
    df = pd.read_excel(new_aluno)
    df.columns = (['nome','a','b','c','nota'])

    df = df[['nome', 'nota']]
    df = df[['nome', 'nota']][6:]
    dados = [[],[]]
    for nome_aluno in df['nome']:
        dados[0].append(nome_aluno)
        
    for nota_aluno in df['nota']:
        dados[1].append(round(nota_aluno,1))
    
    return dados

def importProva1(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importP1.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.prova1 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], prova1 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importP1.html')

def importProva2(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importP2.html')

        dados = tratando_nota(new_aluno)
        
        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.prova2 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], prova2 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importP2.html')

def importProva3(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importP3.html')

        dados = tratando_nota(new_aluno)
        
        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.prova3 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], prova3 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importP3.html')

def importProva4(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importP4.html')

        dados = tratando_nota(new_aluno)
        
        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.prova4 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], prova4 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importP4.html')

def importLista1(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL1.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.lista1 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], lista1 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importL1.html')

def importLista2(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL2.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.lista2 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], lista2 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importL2.html')

def importLista3(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL3.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.lista3 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], lista3 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importL3.html')

def importLista4(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL4.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.lista4 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], lista4 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importL4.html')

def importLista5(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL5.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.lista5 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], lista5 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importL5.html')

def importLista6(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL6.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.lista6 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], lista6 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importL6.html')

def importLista7(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL7.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.lista7 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], lista7 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importL7.html')

def importLista8(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL8.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                aluno.lista8 = dados[1][i]
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i], lista8 = dados[1][i])
                aluno.save()

    return render(request, 'nota/importL8.html')