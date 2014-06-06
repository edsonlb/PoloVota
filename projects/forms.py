#coding: utf-8
from django import forms
from projects.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

class LoginForm(forms.Form):
    liderNome = forms.CharField(max_length='200', required=True)
    liderTelefone = forms.CharField(max_length='20', required=True)
    liderEmail = forms.EmailField(required=True) 

