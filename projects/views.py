from django.shortcuts import render, get_object_or_404

def new(request):
	return render(request, 'projects/projeto.html',
		{'form': ProjetoForm()})