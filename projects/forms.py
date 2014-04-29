#coding: utf-8
from django import forms
from projects.models import Projeto
from django.forms import ModelForm, TextInput, EmailInput
from django.utils.translation import ugettext as _

class ProjetoForm(forms.ModelForm):
	class Meta:
		model = Projeto
		widgets = {
			'tema' :TextInput(attrs={'class':'form-control', 'placeholder':_('Tema'), 'type':'text'}),
			'projeto':TextInput(attrs={'class':'form-control', 'placeholder':_('Link do projeto'), 'type':'text'}),
			'nomeOrientador' :TextInput(attrs={'class':'form-control', 'placeholder':_('Nome do Orientador'), 'type':'text'}),
			'nomeIntegrante': TextInput(attrs={'class':'form-control', 'placeholder':_('Nomes dos Integrantes'), 'type':'text'}),
			'redeSocial': TextInput(attrs={'class':'form-control', 'placeholder':_('Rede Social do grupo ou lider'), 'type':'text'}),
			'modelagem': TextInput(attrs={'class':'form-control', 'placeholder':_('Modelagem'), 'type':'text'}),
			# Dados do Lider
			'nomeLider': TextInput(attrs={'class':'form-control', 'placeholder':_('Nome do Lider'), 'type':'text'}),
			'emailLider': EmailInput(attrs={'class':'form-control', 'placeholder':_('Email do grupo ou lider')}),
			'telefoneLider': TextInput(attrs={'class':'form-control', 'placeholder':_('Telefone do grupo ou Lider'), 'type':'text'}),
			'cpfLider': TextInput(attrs={'class':'form-control', 'placeholder':_('CPF do Lider'), 'type':'text'})
		}