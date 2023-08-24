from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    profissao = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=20)
    numero_filhos = models.IntegerField()
    cidade_residencia = models.CharField(max_length=100)
    jornada_trabalho = models.CharField(max_length=50)
    atividades_fim_semana = models.TextField()

    def __str__(self):
        return self.nome

