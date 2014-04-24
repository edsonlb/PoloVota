# This Python file uses the following encoding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from persons.models import Person
from persons.forms import AvaliadorForm


def listar(request):
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'list.html', {'persons': persons})


def adicionar(request):
    if request.method == 'POST':
        return salvar(request)

    return render(request, 'form.html', {'form': AvaliadorForm()})


def editar(request, pk=None):
    try:
        person = Person.objects.get(pk=pk)
        form = AvaliadorForm(instance=person)
    except:
        return HttpResponseRedirect('/persons/')

    if request.method == 'POST':
        return salvar(request, person)

    return render(request, 'form.html', {'form': form})


def salvar(request, person=None):
    if person:
        form = AvaliadorForm(request.POST, instance=person)
    else:
        form = AvaliadorForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect('/persons/')
    return render(request, 'form.html', {'form': form})
