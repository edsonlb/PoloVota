# This Python file uses the following encoding: utf-8
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from projects.forms import LoginForm

def index(request):
    return render(request, 'index.html')

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form':form})

def save(request):
    return render(request, 'save.html')

def email(request):
    return render(request, 'email.html')

def validation(request):
    return render(request, 'validation.html')

def validation_error(request):
    return render(request, 'validation_error.html')

def email_enviar(email, assunto, corpo):
    corpo = corpo + '\n'+'\n'+'E-MAIL AUTOMÁTICO! NÃO RESPONDA!'
    assunto = 'PoloVota - '+assunto
    send_mail(assunto, corpo, settings.DEFAULT_FROM_EMAIL,[email], fail_silently=False)



