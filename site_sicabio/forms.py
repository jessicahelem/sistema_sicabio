# -*- coding: utf-8 -*-

from django import forms
from django.contrib import messages
from django.shortcuts import redirect

from .models import *
from django.forms import ModelForm


class UsuarioForm(forms.ModelForm):
    Profissional._meta.get_field('password').blank = False
    Profissional._meta.get_field('CPF').blank = False
    Profissional._meta.get_field('email').blank = False
    Profissional._meta.get_field('username').blank = False

    class Meta:
        model = Profissional
        fields = ["username", "nome", "CPF", "email", "password", "especialidade"]

        nome = forms.CharField()

        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Username'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome Completo'}),
            'CPF': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 14, 'placeholder': 'CPF'}),
            'especialidade': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Especialidade'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 8, 'placeholder': 'Senha'}),

        }

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if Profissional.objects.filter(email=email).exists():
            raise forms.ValidationError('Email JÁ EXISTE!')

        return email



    def clean_cpf(self):
        cpf = self.cleaned_data['CPF']
        if Profissional.objects.filter(CPF=cpf).exists():
            forms.ValidationError('CPF JÁ EXISTE!')
        return cpf

    def clean_user(self):
        username = self.cleaned_data['username']
        if Profissional.objects.filter(username=username).exists():
            raise forms.ValidationError('USERNAME JÁ EXISTE!')
        return username
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('SENHA DEVE TER 8 OU MAIS CARACTERES!')
        return password
