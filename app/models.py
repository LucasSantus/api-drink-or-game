from django.db import models

class Desafio(models.Model):

    DESAFIOS=[
        ("f","Fácil"),
        ("m", "Médio"),
        ("d" , "Dificil"),
    ]

    frase = models.TextField(
        max_length=500,
        null=False,
    )

    nivel_desafios = models.CharField(
        verbose_name="Nível dos Desafios: ", 
        null = False,
        max_length=30, 
        choices=DESAFIOS,
    )

    def __str__(self):
        return self.frase

class Regra_Casa(models.Model):
    frase = models.TextField(max_length=500)

    def __str__(self):
        return self.frase
