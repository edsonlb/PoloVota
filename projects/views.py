# This Python file uses the following encoding: utf-8
from projects.forms import ProjectForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse 
from projects.models import Project
from django.shortcuts import render, get_object_or_404
from core.views import email_enviar
from django.conf import settings
from django.db.models import Q


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid(): 
            try:
                project = Project.objects.filter(liderNome=form.data['liderNome'].upper(), liderTelefone=form.data['liderTelefone'], liderEmail=form.data['liderEmail'].upper(), ativo='SIM')[0]
                formulario = ProjectForm(instance=project)
            except: 
                return render(request, 'login.html', {'form': form, 'msg':'Projeto não encontrado. Revise as suas informações.'})

            return render(request, 'formProject.html', {'form': formulario})
        else:
            return render(request, 'login.html', {'form': form, 'msg':'Os dados não são válidos. Revise os campos.'})    
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form, 'msg':'Erro de login.'}) 

def listar(request):
    projects = Project.objects.all().order_by('tema')
    return render(request, 'listProject.html', {'projects': projects})

def prazos(request):
    return render(request, 'prazosProject.html')

def novo(request):
    form = ProjectForm()
    return render(request, 'formProject.html', {'form': form})

def pesquisar(request):
    if request.method == 'POST':
        textoBusca = request.POST.get('textoBusca', 'TUDO').upper()

        try:
            if textoBusca == 'TUDO':
                projects = Project.objects.all().order_by('-tema')
            else:
                projects = Project.objects.filter(
                    (Q(area__contains=textoBusca) |  
                    Q(tema__contains=textoBusca) | 
                    Q(descricao__contains=textoBusca) | 
                    Q(universidadeOrientador__contains=textoBusca) | 
                    Q(liderNome__contains=textoBusca) | 
                    Q(liderEmail__contains=textoBusca) | 
                    Q(liderIntegrantes__contains=textoBusca) | 
                    Q(universidade__contains=textoBusca))).order_by('-tema') 
        except:
            projects = []

        return render(request, 'listProject.html', {'projects': projects, 'textoBusca': textoBusca})
    return HttpResponseRedirect('/')

def salvar(request):
    if request.method == 'POST':

        try:
            project = Project.objects.get(id=request.POST.get('id','0'))   
            form = ProjectForm(request.POST, instance=project)  
        except:
            form = ProjectForm(request.POST)
        
        if form.is_valid():
            project = form.save()

            if project.ativo == 'VAL':
                email_enviar(project.liderEmail, 'Valide seu Email', 'Valide seu email: '+settings.HOST_WWW+'projects/validation/'+str(project.pk)+'/')
                return HttpResponseRedirect('/email/')
            else:
                return HttpResponseRedirect('/save/')
        else:
            return render(request, 'formProject.html', {'form': form})    
    else:
        return HttpResponseRedirect('/')

def validation_ativo(request, numero):
    if numero:
        if numero > 0:
            try:
                project = get_object_or_404(Project, pk=numero, ativo='VAL')
                project.ativo = 'SIM'
                project.save()
            except:
                return HttpResponseRedirect('/validation_error/')    
            
    return HttpResponseRedirect('/validation/')

def mostrar(request, numero):

    if numero:
        if numero > 0:
            try:
                project = get_object_or_404(Project, pk=numero, ativo='SIM')
                form = ProjectForm(instance=project)
                return render(request, 'formProject.html', {'form': form, 'acao':'view'}) 
            except:
                return HttpResponseRedirect('/')    
            
    return HttpResponseRedirect('/')

def ranking(request):
    projects = Project.objects.filter(ativo='SIM').order_by('area', 'tema')
    return render(request, 'rankingProject.html', {'projects': projects})