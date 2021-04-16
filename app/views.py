from django.shortcuts import render
from rest_framework import viewsets
from .models import Desafio, Regra_Casa
from .serializers import DesafioSerializer, Regra_CasaSerializer

class DesafioViewSet(viewsets.ModelViewSet):
    queryset = Desafio.objects.all()
    serializer_class = DesafioSerializer

class Regra_CasaViewSet(viewsets.ModelViewSet):
    queryset = Regra_Casa.objects.all()
    serializer_class = Regra_CasaSerializer
