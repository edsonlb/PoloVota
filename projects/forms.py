#coding: utf-8
from django import forms
from projects.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

class ContactForm1(forms.Form):
    liderNome = forms.CharField(max_length=200, null=False, blank=False)
    liderTelefone = forms.CharField(max_length=20, null=False, blank=False)
    liderEmail = forms.EmailField(null=False, blank=False) 

