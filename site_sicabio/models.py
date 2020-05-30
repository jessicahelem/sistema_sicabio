from enum import Enum

import consultas as consultas
from django.conf import settings
from django.db import models
from django.utils import timezone


class Profissional(models.Model):
    # id_prof = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    user_cpf = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=8)
    especialidade = models.CharField(max_length=100,null=True)


class ImpressaoDigital(models.Model):
    img_path = models.FilePathField(path=None)
    mao_esquerda = models.ForeignKey('MaoEsquerda', on_delete=models.CASCADE,related_name='im_digital')
    mao_direita = models.ForeignKey('MaoDireita', on_delete=models.CASCADE,related_name='im_digital')
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE,related_name='im_digital')


class Paciente(models.Model):
    # id_paciente = models.IntergerField(primary_key=True),
    nome_paciente = models.CharField(max_length=100)
    cpf_paciente = models.CharField(max_length=12)
    imp_digital = models.ForeignKey('ImpressaoDigital',on_delete=models.CASCADE,related_name='imp_digital')
    resultado_perfil = models.ForeignKey('Analise',on_delete=models.CASCADE,related_name='imp_digital')


class Consulta(models.Model):
    # id_consulta = models.IntergerField(primary_key=True, on_delete=models.CASCADE)
    id_profissional = models.ForeignKey('Profissional', on_delete=models.CASCADE,related_name='consulta')
    data = models.DateField(auto_now=False, auto_now_add=False)
    horario = models.TimeField(auto_now=False)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE,related_name='consulta')


class Potencialidade(models.Model):
    TIPOS = (('F', 'Força'),
             ('V', "Velocidade"),
             ('CM', "Coordenação Motora"),
             ('A', "Agilidade"),
             ('R', "Resistência")
             )
    tipo = models.CharField(max_length=1, choices=TIPOS)


class Analise(models.Model):
    #id_analise = models.IntegerField(primary_key=True, on_delete=models.CASCADE, related_name="analise")
    sqtle = models.IntegerField()
    sqtld = models.IntegerField()
    sqtl = models.IntegerField()
    d_dez = models.IntegerField()
    qtd_total_verticilos = models.IntegerField()
    qtd_total_arcos = models.IntegerField()
    qtd_total_presilhas = models.IntegerField()
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE,related_name='paciente')
    Resultado = models.ForeignKey('Potencialidade', on_delete=models.CASCADE,related_name='analise')


class Padrao(models.Model):
    Padroes = (('W', 'Verticilo'),
               ('L', "Presilha"),
               ('A', "Arco"),

               )
    padroes = models.CharField(max_length=1, choices=Padroes)


class MaoEsquerda(models.Model):
    nome_dedo = models.CharField(max_length=100)
    padrao = models.ForeignKey('Padrao', on_delete=models.CASCADE,related_name='mao_esquerda')


class MaoDireita(models.Model):
    nome_dedo = models.CharField(max_length=100)
    padrao = models.ForeignKey('Padrao', on_delete=models.CASCADE, related_name='mao_direita')
