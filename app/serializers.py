from rest_framework import serializers
from .models import Desafio, Regra_Casa

class DesafioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desafio
        fields = [
            "frase",
            "nivel_desafios", 
        ]

class Regra_CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regra_Casa
        fields = [
            "frase",
        ]