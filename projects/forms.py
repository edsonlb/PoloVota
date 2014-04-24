#coding: utf-8
from django import forms
from projects.models import Projeto
from django.forms import ModelForm, TextInput, EmailInput
from django.utils.translation import ugettext as _

class ProjetoForm(forms.ModelForm):
	class Meta:
		model = Projeto
		widgets = {
			'tema' :TextInput(attrs={'placeholder':_('Tema'), 'type':'text'}),
			'projeto':TextInput(attrs={'placeholder':_('Link do projeto'), 'type':'text'}),
			'nomeOrientador' :TextInput(attrs={'placeholder':_('Nome do Orientador'), 'type':'text'}),
			'nomeIntegrante': TextInput(attrs={'placeholder':_('Nomes dos Integrantes'), 'type':'text'}),
			'redeSocial': TextInput(attrs={'placeholder':_('Rede Social'), 'type':'text'}),
			'modelagem': TextInput(attrs={'placeholder':_('Modelagem'), 'type':'text'}),
			# Dados do Lider
			'nomeLider': TextInput(attrs={'placeholder':_('Nome do Lider'), 'type':'text'}),
			'emailLider': EmailInput(attrs={'placeholder':_('Email')}),
			'telefoneLider': TextInput(attrs={'placeholder':_('Telefone do Lider'), 'type':'text'}),
			'cpfLider': TextInput(attrs={'placeholder':_('CPF do Lider'), 'type':'text'})
		}