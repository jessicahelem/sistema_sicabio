from enum import Enum
from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, nome, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            nome=nome,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, nome, password=None, **extra_fields):
        return self._create_user(username, email, nome, password, False, False, **extra_fields)

    def create_superuser(self, username, email, nome, password=None, **extra_fields):
        return self._create_user(username, email, nome, password, True, True, **extra_fields)


class Profissional(PermissionsMixin,AbstractBaseUser):
    # id_prof = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200, unique=True, blank=False, null=False)
    CPF = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()
    especialidade = models.CharField(max_length=100, null=True)
    # paciente = models.ListField('Paciente', on_delete=models.CASCADE,null=True,default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email", 'nome']

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True




class Impressao(models.Model):
    img_path = models.ImageField(upload_to='impressoes', null=True)
    mao = models.CharField(max_length=200,null=False)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='im_digital')
   # padrao = models.ForeignKey('Padrao',on_delete=models.CASCADE,null=True,default=True)
    dedo = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.id)


class Paciente(models.Model):
    # id_paciente = models.IntergerField(primary_key=True),
    foto = models.ImageField(upload_to='pacientes', null=True, default='media/avatar.png',blank='media/avatar.png')
    nome_paciente = models.CharField(max_length=100, null=False)
    cpf_paciente = models.CharField(max_length=12, null=False,unique=True)
    dt_nascimento = models.DateField(auto_now = False,null=False)
    profissional = models.ForeignKey('Profissional',on_delete=models.CASCADE,null=False,default=False)
    # imp_digital = models.ForeignKey('ImpressaoDigital',on_delete=models.CASCADE,related_name='imp_digital',default=True,null=True)
    # resultado_perfil = models.ForeignKey('Analise',on_delete=models.CASCADE,related_name='imp_digital',default=True,null=True)

    def __str__(self):
        return str(self.nome_paciente)


class Consulta(models.Model):
    # id_consulta = models.IntergerField(primary_key=True, on_delete=models.CASCADE)
    data = models.DateField(auto_now=False)
    horario = models.TimeField(auto_now=False)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='consulta')
    profissional= models.ForeignKey('Profissional', on_delete=models.CASCADE, related_name='consulta')

    def __str__(self):
        return str(self.id)


class Potencialidade(models.Model):
    TIPOS = (('F', 'Força'),
             ('V', "Velocidade"),
             ('CM', "Coordenação Motora"),
             ('A', "Agilidade"),
             ('R', "Resistência")
             )
    tipo = models.CharField(max_length=1, choices=TIPOS)


class Analise(models.Model):
    # id_analise = models.IntegerField(primary_key=True, on_delete=models.CASCADE, related_name="analise")
    sqtle = models.IntegerField()
    sqtld = models.IntegerField()
    sqtl = models.IntegerField()
    d_dez = models.IntegerField()
    qtd_total_verticilos = models.IntegerField()
    qtd_total_arcos = models.IntegerField()
    qtd_total_presilhas = models.IntegerField()
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='paciente')
    Resultado = models.ForeignKey('Potencialidade', on_delete=models.CASCADE, related_name='analise')

    def __str__(self):
        return str(self.id)


class Padrao(models.Model):
    Padroes = (('W', 'Verticilo'),
               ('L', "Presilha"),
               ('A', "Arco"),

               )
    padroes = models.CharField(max_length=1, choices=Padroes)

