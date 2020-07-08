# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.forms import ModelForm


class UsuarioForm(forms.ModelForm):
    Profissional._meta.get_field('password').blank = False
    Profissional._meta.get_field('CPF').blank = False
    Profissional._meta.get_field('email').blank = False
    Profissional._meta.get_field('username').blank = False



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



    def save(self, commit=True):
          user = super(UsuarioForm, self).save(commit=False)
          user.set_password(self.cleaned_data['password'])
          if commit:
              user.save()
          return user

    def clean_email(self):
        email=self.cleaned_data['email']
        if Profissional.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um usuário com esse email.')
        return email

    def clean_cpf(self):
        cpf = self.cleaned_data['CPF']
        if Profissional.objects.filter(CPF=cpf).exists():
            raise forms.ValidationError('CPF já existe.')
        return cpf

    def clean_user(self):
        username = self.cleaned_data['username']
        if Profissional.objects.filter(username=username).exists():
            raise forms.ValidationError('Username já existe.')
        return username