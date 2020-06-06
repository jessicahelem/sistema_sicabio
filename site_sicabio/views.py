from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from rest_framework.compat import authenticate

from .form import *


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def index(request):
    return render(request,'cadastro.html')

def cadastrar_profissional(request):
    form  = UsuarioForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, "templates/cadastro.html",context)

def login(request):
    return render(request,"login.html",{})

@csrf_protect
def submit_login(request):
    if request.POST:
        usercpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        user = authenticate(usercpf=usercpf,senha=senha)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Usuário e senha Inválidos. Por favor tente novamente.  ')
    return redirect('/login/')
