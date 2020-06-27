# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.forms import ModelForm


class UsuarioForm(forms.ModelForm):
    Profissional._meta.get_field('password').blank = False
    Profissional._meta.get_field('CPF').blank = False
    Profissional._meta.get_field('nome').blank = False

    class Meta:
        model = Profissional
        fields = ["username","nome", "CPF", "email", "password", "especialidade"]

        nome = forms.CharField()

        widgets = {
            "username":forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder':'Username'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome Completo'}),
            'CPF': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 12, 'placeholder': 'CPF'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 8, 'placeholder': 'Senha'}),
            'especialidade': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Especialidade'}),
            }

        error_messages = {
            'nome': {
                'required': 'Este campo é obrigatório'
            },
            'CPF': {
                'required': 'Este campo é obrigatório'

            },

            'password': {
                'required': 'Este campo é obrigatório'

            },
            'especialidade': {
                'required': 'Este campo é obrigatório'

            },
            'username': {
                'required': 'Este campo é obrigatório'
            },

            'email':{
                'required': 'Este campo é obrigatório.'
            },



        }

    def save(self, commit=True):
          user = super(UsuarioForm, self).save(commit=False)
          user.set_password(self.cleaned_data['password'])
          if commit:
              user.save()
          return user


class PacienteForm(forms.Form):

    class Meta:
        model = Paciente
        fields = ['nome_paciente', 'cpf_paciente','idade','foto']

        # foto = forms.ImageField()
        # nome_paciente = forms.CharField(label='Nome Completo',widget=forms.Textarea)
        # cpf_paciente = forms.CharField(label='CPF',widget=forms.Textarea)

        widgets = {'nome_paciente': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome'}),
                   'cpf_paciente': forms.TextInput(
                    attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'CPF'}),
                   'idade':forms.TextInput(attrs={'class':'form-control','placeholder':'Idade'}),
                   'foto': forms.ImageField(),

                   }
