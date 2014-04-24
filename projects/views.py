from projects.forms import ProjetoForm
from projects.models import Projeto
from django.shortcuts import render, get_object_or_404

def listar(request):
	return render(request, 'projeto.html', {'form': ProjetoForm()})