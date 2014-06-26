# This Python file uses the following encoding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.db.models import Q
from persons.models import Person
from persons.forms import LoginForm

def loginRedirect(request):
    form = LoginForm()
    return render(request, 'loginPerson.html', {'form': form})

# https://docs.djangoproject.com/en/1.6/topics/auth/default/#django.contrib.auth.login
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid(): 
            try:         
                print form.data['email']   
                print form.data['password']
                user = authenticate(email=form.data['email'], password=form.data['password'])
                print user
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return render(request, 'votaProject.html')
                    else:
                        return render(request, 'loginPerson.html', {'form': form, 'msg':'Conta desativada.'})
                else:
                    return render(request, 'loginPerson.html', {'form': form, 'msg':'Login Inválido.'})

            except: 
                return render(request, 'loginPerson.html', {'form': form, 'msg':'Projeto não encontrado. Revise as suas informações. Em caso de problemas, envie um e-mail para a lista do Grupo.'})

            
        else:
            return render(request, 'loginPerson.html', {'form': form, 'msg':'Os dados não são válidos. Revise os campos. Em caso de problemas, envie um e-mail para a lista do Grupo.'})    
    else:
        form = LoginForm()
        return render(request, 'loginPerson.html', {'form': form, 'msg':'Erro de login.'}) 

def listar(request):
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'listPerson.html', {'persons': persons})

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
