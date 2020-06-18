from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from rest_framework.compat import authenticate

from .forms import *


@login_required(login_url='/login/')
def logout_user(request):

    logout(request)
    return redirect('/login')

@csrf_protect
def form_paciente(request):
    form = PacienteForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/base_paciente')
    return render(request, "base_paciente.html", context)


def list_all_pacientes(request):
    paciente= Paciente.objects.filter()
    return render(request,'lista_pacientes.html',{'paciente':paciente})

@login_required(login_url='/login/')
def index(request):
    return render(request, 'tela_principal.html')


@csrf_protect
def cadastro(request):
    form = UsuarioForm(request.POST or None)
    context={'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/cadastro')
    return render(request, "cadastro.html", context)


def do_login(request):
    return render(request,'login.html')

def menu_paciente(request):
    return  render(request,'menu_paciente.html')
@csrf_protect
def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Usuário e senha inválidos. Por favor, tente novamente.')
    return redirect('/login/')


def list_user(request):
    usuario = Profissional.objects.filter(user=request.user)
    return render(request,'lista_pacientes.html',{'usuario':usuario})


def pacientes_detalhes(request,id):
    paciente=Paciente.objects.get(id=id)

    return render(request,"detalhes_paciente.html",{'paciente':paciente})