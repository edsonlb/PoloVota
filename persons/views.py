# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from django.db.models import Q
from persons.models import Person

def listar(request):
    #persons = Person.objects.all()

    # TESTE LOCAL PARA VERIFICAR SE A TABELA ESTA LISTANDO
    persons = []
    persons.append(Person(first_name='NOME1', email='MAIL1', empresa='EMPRESA1'))
    persons.append(Person(first_name='NOME2', email='MAIL2', empresa='EMPRESA2'))

    return render(request, 'list.html', {'persons': persons})
