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

from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import EdificioSerializer, DepartamentoSerializer

class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
