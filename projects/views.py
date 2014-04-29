from projects.forms import ProjetoForm
from django.http import HttpResponseRedirect, HttpResponse 
from projects.models import Projeto
from django.shortcuts import render, get_object_or_404

def listar(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def new(request):
	return render(request, 'projeto.html', {'form': ProjetoForm()})

def create(request):
	form = ProjetoForm(request.POST)
	if not form.is_valid():
		print "sakpodpkad===================="
		return render(request, 'projeto.html', {'form': ProjetoForm()})

	obj = form.save()
	return HttpResponseRedirect('/projects/%d/' % obj.pk)

def detail(request, pk):
	project = get_object_or_404(projects, pk=pk)
	return render(request, 'projects_detal.html',
		{'project': project})