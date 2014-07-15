#coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from persons.models import Person, PersonVote
from persons.forms import LoginForm
from projects.models import Project
from projects.forms import ProjectForm

ETAPA = 'E1'

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

# ADMINISTRATIVO ===================================================

def loginRedirect(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/persons/initial/')
    else:
        form = LoginForm()
        return render(request, 'loginPerson.html', {'form': form})

def logoutRedirect(request):
    logout(request)
    return HttpResponseRedirect('/persons/login/')

@login_required(login_url='/persons/login/')
def loginInicial(request):
    #projects = Project.objects.raw("select p.* from projects_project p where id not in (select p.id from projects_project  p inner join persons_personvote pv on (pv.project_id = p.id and pv.etapa like '%%%s%%' and pv.person_id = %d) where p.ativo = 'SIM') and p.ativo = 'SIM' order by p.area, p.tema"%(ETAPA,request.user.pk))
    projects = Project.objects.filter(person_id=request.user.pk)
    return render(request, 'votaProject.html', {'projects':projects, 'title':'VOTE'})

@login_required(login_url='/persons/login/')
def loginVoted(request):
    projects = Project.objects.raw("select p.* from projects_project p inner join persons_personvote pv on (pv.project_id = p.id and pv.etapa like '%%%s%%' and pv.person_id = %d) where p.ativo = 'SIM' order by p.area, p.tema"%(ETAPA,request.user.pk))
    return render(request, 'votaProject.html', {'projects':projects, 'title':'JÁ VOTADOS'})

@login_required(login_url='/persons/login/')
def show(request, pk=None):
    project = Project.objects.get(pk=pk)
    try:
        avaliacao = PersonVote.objects.get(person_id=request.user.pk, project_id=pk)
    except:  
        avaliacao = PersonVote()

    formulario = ProjectForm(instance=project)
    return render(request, 'formProject.html', {'form':formulario, 'vote':True, 'avaliacao':avaliacao.nota})

@login_required(login_url='/persons/login/')
def saveScore(request):
    if request.method == 'POST':
        project = request.POST.get('id','0')
        nota = request.POST.get('nota','1')

        try:
            voto = PersonVote.objects.get(person_id=request.user.pk, project_id=project)
        except:
            voto = PersonVote(person_id=request.user.pk, project_id=project)

        voto.nota = nota
        voto.etapa = ETAPA
        voto.save()
        
        return HttpResponseRedirect('/persons/initial/')    
    else:
        return HttpResponseRedirect('/persons/login/')

@login_required(login_url='/persons/login/')
def ranking(request):
    sql = "select  avg(nota) as avg, pv.* from persons_personvote pv inner join projects_project p on (p.id = pv.project_id and p.ativo='SIM' and p.area='INFORMÁTICA') where pv.etapa like '%%%s%%' GROUP BY pv.project_id order by avg(nota) desc LIMIT 15"%(ETAPA)
    projectsInformatica = PersonVote.objects.raw(sql.decode('utf-8'))[:15]
    sql = "select  avg(nota) as avg, pv.* from persons_personvote pv inner join projects_project p on (p.id = pv.project_id and p.ativo='SIM' and p.area='MECÂNICA') where pv.etapa like '%%%s%%' GROUP BY pv.project_id order by avg(nota) desc LIMIT 15"%(ETAPA)
    projectsMecanica = PersonVote.objects.raw(sql.decode('utf-8'))[:15]
    sql = "select  avg(nota) as avg, pv.* from persons_personvote pv inner join projects_project p on (p.id = pv.project_id and p.ativo='SIM' and p.area='ELETRÔNICA') where pv.etapa like '%%%s%%' GROUP BY pv.project_id order by avg(nota) desc LIMIT 15"%(ETAPA)
    projectsEletronica = PersonVote.objects.raw(sql.decode('utf-8'))[:15]
    
    return render(request, 'rankingParcial.html', {
        'projectsInformatica': projectsInformatica, 
        'projectsMecanica': projectsMecanica,
        'projectsEletronica': projectsEletronica})


# https://docs.djangoproject.com/en/1.6/topics/auth/default/#django.contrib.auth.login
# https://docs.djangoproject.com/en/1.6/topics/auth/default/
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid(): 
            #try:
            user = authenticate(username=form.data['email'].upper(), password=form.data['password'].upper())
            print user
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/persons/initial/')
                else:
                    return render(request, 'loginPerson.html', {'form': form, 'msg':'Conta desativada.'})
            else:
                return render(request, 'loginPerson.html', {'form': form, 'msg':'Login Inválido.'})

            #except: 
            #    return render(request, 'loginPerson.html', {'form': form, 'msg':'Erro de Login! Revise todas as informações e tente novamente.'})   
        else:
            return render(request, 'loginPerson.html', {'form': form, 'msg':'Os dados não são válidos. Revise os campos. Em caso de problemas, envie um e-mail para a lista do Grupo.'})    
    else:
        form = LoginForm()
        return render(request, 'loginPerson.html', {'form': form, 'msg':'Erro de login.'}) 

