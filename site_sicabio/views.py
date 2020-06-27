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
@login_required(login_url='/login/')
def form_paciente(request):
    paciente_id = request.GET.get('id')

    if paciente_id:
        paciente = Paciente.objects.get(id=paciente_id)
        if paciente.profissional == request.user:
            return render(request,'cadastrar_paciente.html',{'paciente':paciente})

    return render(request,'cadastrar_paciente.html')

@login_required(login_url='/login/')
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
            return redirect('/login')
    return render(request, "cadastro.html", context)


def do_login(request):
    return render(request,'login.html')
@login_required(login_url='/login/')
def menu_paciente(request):
    return render(request,'menu_paciente.html')
@csrf_protect
def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        profissional = authenticate(username=username, password=password)

        if profissional is not None:
            login(request,profissional)
            return redirect('/')
        else:
            messages.error(request,'Usuário e senha inválidos. Por favor, tente novamente.')
    return redirect('/login/')

@login_required(login_url='/login/')
def list_user(request):
    paciente = Paciente.objects.filter(profissional =request.user)

    return render(request,'lista_pacientes.html',{'paciente':paciente})

@login_required(login_url='/login/')
def pacientes_detalhes(request,id):

    paciente=Paciente.objects.get(id=id,profissional=request.user)

    return render(request,"detalhes_paciente.html",{'paciente':paciente})

@login_required(login_url='/login/')
def inserir_digital(request,id):
    paciente = Paciente.objects.get(id=id)
    return render(request,'inserir_digital.html',{'paciente':paciente})

@login_required(login_url='/login/')
def set_paciente(request):

    nome_paciente = request.POST.get('nome_paciente')
    cpf_paciente = request.POST.get('cpf_paciente')
    idade = request.POST.get('idade')
    file = request.FILES.get('file')
    paciente_id = request.POST.get('paciente-id')
    prof = request.user

    if paciente_id:
        paciente = Paciente.objects.get(id=paciente_id)
        if prof == paciente.profissional:
            paciente.nome_paciente = nome_paciente
            paciente.cpf_paciente = cpf_paciente
            paciente.idade = idade
            if file:
                paciente.foto = file
            paciente.save()
    else:
        paciente= Paciente.objects.create(foto=file,nome_paciente=nome_paciente,cpf_paciente=cpf_paciente,idade=idade,profissional=prof)

    return redirect('../pacientes/')

@login_required(login_url='/login/')
def cadastrar_digital(request,id):
  # #  mao_esq = ImpressaoDigital.mao_esquerda
  #   img_path =request.FILES.get('file')
  #   mao_esquerda = request.GET.get('mao_esquerda')
  #   mao_direita = request.GET.get('mao_direita')
  #   paciente = request.GET.get('paciente')
  #   digital = ImpressaoDigital.objects.create(img_path=img_path,mao_esquerda=mao_esquerda,mao_direita=mao_direita,paciente=paciente)

    paciente = Paciente.objects.get(id=id)
    return render(request,'up_impressao.html',{'paciente':paciente})

@login_required(login_url='/login/')
def delete_paciente(request,id):
    paciente=Paciente.objects.get(id=id)
    if paciente.profissional == request.user:
        paciente.delete()
    return redirect('../../pacientes/')