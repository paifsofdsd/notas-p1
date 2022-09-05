from django.contrib import admin

from .models import Aluno, NotaAluno

# Register your models here.

admin.site.register(Aluno)
admin.site.register(NotaAluno)