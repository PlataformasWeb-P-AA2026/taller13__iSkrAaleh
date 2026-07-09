from django.shortcuts import render
from .models import Edificio, Departamento

def index(request):
    return render(request, 'index.html')

def listar_edificios(request):
    edificios = Edificio.objects.all()
    return render(request, 'edificios.html', {'edificios': edificios})

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos.html', {'departamentos': departamentos})
