# This Python file uses the following encoding: utf-8
from projects.forms import ProjectForm
from django.http import HttpResponseRedirect, HttpResponse 
from projects.models import Project
from django.shortcuts import render, get_object_or_404
from core.views import email_enviar
from django.conf import settings
from django.db.models import Q

def login(request):
    liderNome = request.POST.get('liderNome','0')
    liderTelefone = request.POST.get('liderTelefone','0')
    liderEmail = request.POST.get('liderEmail','0')

    try:
        project = Project.objects.get(liderNome=liderNome, liderTelefone=liderTelefone, liderEmail=liderEmail )
    except: 
        colocar aqui um redirecionamento para uma tela de erro
        
    form = ProjectForm() colocar aqui a criação do form para ele poder editar e salvar
    form.full_clean()
    return render(request, 'formProject.html', {'form': form})

def listar(request):
    projects = Project.objects.all().order_by('tema')
    return render(request, 'listProject.html', {'projects': projects})

def prazos(request):
    return render(request, 'prazosProject.html')

def novo(request):
    form = ProjectForm()
    form.full_clean()
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
        form = ProjectForm(request.POST)
        
        if form.is_valid():
            project = Project(**form.cleaned_data)

            project.save()

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