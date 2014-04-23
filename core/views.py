# This Python file uses the following encoding: utf-8
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')