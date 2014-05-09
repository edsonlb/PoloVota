# This Python file uses the following encoding: utf-8
from projects.forms import ProjectForm
from django.http import HttpResponseRedirect, HttpResponse 
from projects.models import Project
from django.shortcuts import render, get_object_or_404


def listar(request):
    projects = Project.objects.all().order_by('tema')
    return render(request, 'listProject.html', {'projects': projects})

def novo(request):
    return render(request, 'formProject.html', {'form': ProjectForm()})

def create(request):
    form = ProjetoForm(request.POST)
    if not form.is_valid():
        return render(request, 'listProject.html', {'form': ProjetoForm()})

    obj = form.save()
    return HttpResponseRedirect('/projects/%d/' % obj.pk)

def detail(request, pk):
    project = get_object_or_404(projects, pk=pk)
    return render(request, 'form.html',{'project': project})