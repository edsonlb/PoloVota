# This Python file uses the following encoding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from persons.models import Person
from persons.forms import AvaliadorForm

def listar(request):
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'list.html', {'persons': persons})

def editar(request, pk = 0):
    try:
        person = Person.objects.get(pk=pk)
        form = AvaliadorForm(instance=person)
    except:
        return HttpResponseRedirect('/persons/')

    return render(request, 'form.html', {'form': form})

def salvar(request):
    if request.method == 'POST':
        form = AvaliadorForm(request.POST)
        
        print "%s" % repr(form.errors)

        if form.is_valid():
            #form.save()
            person = Person(**form.cleaned_data)
            person.save()
            return HttpResponseRedirect('/persons/')
        else:
            return render(request, 'form.html', {'form': form})   
    else:
        return render(request, 'form.html', {'form': AvaliadorForm()})
    
