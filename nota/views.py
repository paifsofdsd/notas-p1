from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Aluno, NotaAluno
from django.contrib import messages
import pandas as pd
from django.contrib.auth.decorators import user_passes_test


def index(request):
    return redirect('resolution')

def resolution(request):
    print( lambda u: u.is_superuser )
    data = {}
    colunas = ('Nome', 'Turma', 'Prova 1', 
    'Lista 1', 'Lista 2', 'Prova 2', 'Lista 3',
    'Lista 4', 'Prova 3', 'Lista 5', 'Lista 6',
    'Prova 4', 'Lista 7', 'Lista 8')

    lista = []
    for i in Aluno.objects.all():
        i.nome = i.nome.title()
        lista.append(i)

    alunos_ordenados = sorted(lista, key = lambda x: x.nome)

    data['alunos'] = alunos_ordenados
    data['colunas'] = colunas

    return render(request, 'nota/resolution.html', data)

def notasAcumuladas(request):

    data = {}
    colunas = ('Nome', 'Turma', 'AB1', 'AB2', 
    'Reav', 'Final', 'Média', 'Situação',)

    lista = []
    for i in NotaAluno.objects.all():
        i.nome = i.nome.title()
        lista.append(i)

    alunos_ordenados = sorted(lista, key = lambda x: x.nome)

    data['alunos'] = alunos_ordenados
    data['colunas'] = colunas

    return render(request, 'nota/notas.html', data)

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def importProva(request):
    if request.method == 'POST':
        requested_test = request.POST['prova']
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importP4.html')

        dados = tratando_nota(new_aluno)
        
        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                setattr(aluno, requested_test, dados[1][i])
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i])
                setattr(aluno, requested_test, dados[1][i])
                aluno.save()

    return render(request, 'nota/importP'+request.path[-2]+'.html')

@user_passes_test(lambda u: u.is_superuser)
def importLista(request):
    if request.method == 'POST':
        requested_list = request.POST['lista']
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importL1.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            try:
                aluno = Aluno.objects.get(nome=dados[0][i])
                setattr(aluno, requested_list, dados[1][i])
                aluno.save()
            except:
                aluno = Aluno(nome = dados[0][i])
                setattr(aluno, requested_list, dados[1][i])
                aluno.save()

    return render(request, 'nota/importL'+request.path[-2]+'.html')

def calcularMedia(dados, index):
    aluno = NotaAluno.objects.get(nome = dados[0][index])
    
    if aluno.reav > aluno.ab2 and aluno.ab2 <= aluno.ab1:
        aluno.mediaFinal = round(((aluno.reav + aluno.ab1)/2), 2)
    elif aluno.reav > aluno.ab1 and aluno.ab1 <= aluno.ab2:
        aluno.mediaFinal = round(((aluno.reav + aluno.ab2)/2), 2)
    else:
        aluno.mediaFinal = round(((aluno.ab1 + aluno.ab2)/2), 2)

    if aluno.mediaFinal >= 7:
        aluno.situacao = 'APROVADO'
    elif aluno.mediaFinal < 5:
        aluno.situacao = 'REPROVADO'

    aluno.save()

@user_passes_test(lambda u: u.is_superuser)
def importReav(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importReav.html')

        dados = tratando_nota(new_aluno)        

        for i in range(len(dados[0])):
            dados[1][i] = round((dados[1][i] * 100) / 100, 2)
            try:
                aluno = NotaAluno.objects.get(nome=dados[0][i])
                aluno.reav = round(dados[1][i], 2)
                aluno.save()
            except:
                aluno = NotaAluno(nome = dados[0][i], reav = dados[1][i])
                aluno.save()
            
            calcularMedia(dados, i)
            

    return render(request, 'nota/importReav.html')

def calcularFinal(dados, index):
    aluno = NotaAluno.objects.get(nome = dados[0][index])

    final = (((6 * aluno.mediaFinal) + (4 * aluno.final))/10)

    if final >= 5.50 or final > aluno.mediaFinal:
        aluno.mediaFinal = round( final, 2)
        if(final >= 5.50):
            aluno.situacao = 'APROVADO'
    else:
        aluno.situacao = 'REPROVADO'

    aluno.save()

@user_passes_test(lambda u: u.is_superuser)
def importFinal(request):
    if request.method == 'POST':
        new_aluno = request.FILES['myfile']

        if not new_aluno.name.endswith('xls'):
            messages.info(request, 'wrong format')
            return render(request, 'nota/importFinal.html')

        dados = tratando_nota(new_aluno)

        for i in range(len(dados[0])):
            dados[1][i] = round((dados[1][i] * 100) / 100, 2)
            try:
                aluno = NotaAluno.objects.get(nome=dados[0][i])
                aluno.final = round(dados[1][i], 2)
                aluno.save()
            except:
                aluno = NotaAluno(nome = dados[0][i], final = dados[1][i])
                aluno.save()
            
            calcularFinal(dados, i)
            

    return render(request, 'nota/importFinal.html')

def calcularMediaFinal(aluno):
    alunoF = NotaAluno.objects.get(nome = aluno.nome)
    alunoF.mediaFinal = round(((alunoF.ab1 + alunoF.ab2)/2), 2)
    print(alunoF.mediaFinal)
    alunoF.save()

@user_passes_test(lambda u: u.is_superuser)
def calcularAB1(request):
    if request.method == 'POST':
        alunos = Aluno.objects.all()

        for aluno in alunos:
            try:
                alunoF = NotaAluno.objects.get(nome = aluno.nome)
                alunoF.ab1 = round(((((aluno.prova1 + aluno.prova2)*7)/20) + (((aluno.lista1 + aluno.lista2 + aluno.lista3 + aluno.lista4)*3)/58)), 2)
                alunoF.save()
            except:
                notaAB1 = round(((((aluno.prova1 + aluno.prova2)*7)/20) + (((aluno.lista1 + aluno.lista2 + aluno.lista3 + aluno.lista4)*3)/58)), 2)
                alunoF = NotaAluno(nome = aluno.nome, ab1 = notaAB1)
                alunoF.save()

            calcularMediaFinal(aluno)
            

    return render(request, 'nota/calcularAB1.html')

@user_passes_test(lambda u: u.is_superuser)
def calcularAB2(request):
    if request.method == 'POST':
        alunos = Aluno.objects.all()

        for aluno in alunos:
            try:
                alunoF = NotaAluno.objects.get(nome = aluno.nome)
                alunoF.ab2 = round(((((aluno.prova3 + aluno.prova4)*7)/20) + (((aluno.lista5 + aluno.lista6 + aluno.lista7 + aluno.lista8)*3)/66)), 2)
                alunoF.mediaFinal = round( ((alunoF.ab1 + alunoF.ab2)/2), 2)
                if alunoF.mediaFinal >= 7:
                    alunoF.situacao = 'APROVADO'
                alunoF.save()
            except:
                notaAB2 = round(((((aluno.prova3 + aluno.prova4)*7)/20) + (((aluno.lista5 + aluno.lista6 + aluno.lista7 + aluno.lista8)*3)/66)), 2)
                alunoF = NotaAluno(nome = aluno.nome, ab1 = notaAB2)
                alunoF.mediaFinal = round( ((alunoF.ab1 + alunoF.ab2)/2), 2)
                if alunoF.mediaFinal >= 7:
                    alunoF.situacao = 'APROVADO'
                alunoF.save()

    return render(request, 'nota/calcularAB2.html')

def searchNotaIndividual(request):
    if request.method == 'POST':
        search = request.POST['search']

        if request.POST['select'] == 'nome':
            result_search = Aluno.objects.filter(nome__contains=search)
        elif request.POST['select'] == 'turma':
            result_search = Aluno.objects.filter(turma=search.upper())

        dados = {}
        colunas = ('Nome', 'Turma', 'Prova 1', 
        'Lista 1', 'Lista 2', 'Prova 2', 'Lista 3',
        'Lista 4', 'Prova 3', 'Lista 5', 'Lista 6',
        'Prova 4', 'Lista 7', 'Lista 8')

        lista = []
        for i in result_search:
            i.nome = i.nome.title()
            lista.append(i)

        alunos_ordenados = sorted(lista, key = lambda x: x.nome)

        dados['alunos'] = alunos_ordenados
        dados['colunas'] = colunas
        
        return render(request, 'nota/resolution.html', dados)
    else:
        return redirect('resolution')
        
def searchNotaGeral(request):
    if request.method == 'POST':
        search = request.POST['search']

        if request.POST['select'] == 'nome':
            result_search = NotaAluno.objects.filter(nome__contains=search)
        elif request.POST['select'] == 'turma':
            result_search = NotaAluno.objects.filter(turma=search.upper())

        dados = {}
        colunas = ('Nome', 'Turma', 'AB1', 'AB2', 
        'Reav', 'Final', 'Média', 'Situação',)

        lista = []
        for i in result_search:
            i.nome = i.nome.title()
            lista.append(i)

        alunos_ordenados = sorted(lista, key = lambda x: x.nome)

        dados['alunos'] = alunos_ordenados
        dados['colunas'] = colunas
        
        return render(request, 'nota/notas.html', dados)
    else:
        return redirect('notas')