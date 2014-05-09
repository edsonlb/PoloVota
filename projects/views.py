# This Python file uses the following encoding: utf-8
from projects.forms import ProjetoForm
from django.http import HttpResponseRedirect, HttpResponse 
from projects.models import Projeto
from django.shortcuts import render, get_object_or_404

def listar(request):
    project = Projeto.objects.all().order_by('first_name')
    return render(request, 'list.html', {'project': project})

def new(request):
    return render(request, 'list.html', {'form': ProjetoForm()})

def create(request):
    form = ProjetoForm(request.POST)
    if not form.is_valid():
        return render(request, 'list.html', {'form': ProjetoForm()})

    obj = form.save()
    return HttpResponseRedirect('/projects/%d/' % obj.pk)

def detail(request, pk):
    project = get_object_or_404(projects, pk=pk)
    return render(request, 'form.html',{'project': project})