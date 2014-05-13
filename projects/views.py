# This Python file uses the following encoding: utf-8
from projects.forms import ProjectForm
from django.http import HttpResponseRedirect, HttpResponse 
from projects.models import Project
from django.shortcuts import render, get_object_or_404


def listar(request):
    projects = Project.objects.all().order_by('tema')
    return render(request, 'listProject.html', {'projects': projects})

def novo(request):
    form = ProjectForm()
    form.full_clean()
    return render(request, 'formProject.html', {'form': form})

def salvar(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        
        if form.is_valid():
            project = Project(**form.cleaned_data)
            project.save()
            return HttpResponseRedirect('/projects/new/')
        else:
            return render(request, 'formPessoaJuridica.html', {'form': form})    
    else:
        return render(request, 'formPessoaFisica.html', {'form': PessoaFisicaForm()})





    form = ProjetoForm(request.POST)
    if not form.is_valid():
        return render(request, 'formProject.html', {'form': ProjetoForm()})

    obj = form.save()
    return HttpResponseRedirect('/projects/%d/' % obj.pk)

def detail(request, pk):
    project = get_object_or_404(projects, pk=pk)
    return render(request, 'form.html',{'project': project})