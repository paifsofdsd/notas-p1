from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.CharField(null=True, max_length=2)

    prova1 = models.DecimalField(default=0.0, max_digits=2, decimal_places=2)
    lista1 = models.IntegerField(default=0)
    lista2 = models.IntegerField(default=0)

    prova2 = models.DecimalField(default=0.0, max_digits=2, decimal_places=2)
    lista3 = models.IntegerField(default=0)
    lista4 = models.IntegerField(default=0)

    prova3 = models.DecimalField(default=0.0, max_digits=2, decimal_places=2)
    lista5 = models.IntegerField(default=0)
    lista6 = models.IntegerField(default=0)

    prova4 = models.DecimalField(default=0.0, max_digits=2, decimal_places=2)
    lista7 = models.IntegerField(default=0)
    lista8 = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class NotaAluno(models.Model):
    nome = models.CharField(max_length=100)

    ab1 = models.DecimalField(default=0.0, max_digits=2, decimal_places=2)
    ab2 = models.DecimalField(default=0.0, max_digits=2, decimal_places=2)
    reav = models.DecimalField(default=0.0, max_digits=2, decimal_places=2)
    final = models.DecimalField(default=0.0, max_digits=2, decimal_places=2)

    situacao = models.CharField(max_length=20, default='EM ANÁLISE')