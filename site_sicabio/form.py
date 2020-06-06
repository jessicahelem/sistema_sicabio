# -*- coding: utf-8 -*-

from django import forms
from .models import *


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ["nome", "user_cpf", "email","senha","especialidade"]
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control','maxlenght':255}),
            'user_cpf':forms.TextInput(attrs={'class':'form-control','maxlenght':255}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 255}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'maxlenght': 255}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 255}),

        }
        error_messages = {
            'nome':{
                'required': 'Este campo é obrigatório'
            },
            'user_cpf':{
                'required':'Este campo é obrigatório.'
            },
            'email':{
                'required':'Este campo é obrigatório.'
            },
            'senha': {
                'required': 'Este campo é obrigatório.'
            },
            'especialidade': {
                'required': 'Este campo é obrigatório.'
            },

        }
