from datetime import date
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from rest_framework.authentication import authenticate

from .forms import *


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login')


@csrf_protect
@login_required(login_url='/login/')
def form_paciente(request):
    id_paciente = request.GET.get('id')

    if id_paciente:
        paciente = Paciente.objects.get(id=id_paciente)
        if paciente.profissional == request.user:
            return render(request, 'base_paciente.html', {'paciente': paciente})

    return render(request, 'base_paciente.html')


@login_required(login_url='/login/')
def list_all_pacientes(request):
    paciente = Paciente.objects.filter()
    return render(request, 'lista_pacientes.html', {'paciente': paciente})


@login_required(login_url='/login/')
def index(request):
    return render(request, 'tela_principal.html')


@csrf_protect
def cadastro(request):
    form = UsuarioForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Dados inseridos com sucesso!")

            return redirect('/cadastro/')
    return render(request, "cadastro.html", context)


def do_login(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def menu_paciente(request):
    return render(request, 'menu_paciente.html')


@csrf_protect
def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        profissional = authenticate(username=username, password=password)

        if profissional is not None:
            login(request, profissional)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválidos. Por favor, tente novamente.')
    return redirect('/login/')


@login_required(login_url='/login/')
def list_user(request):


    busca = request.GET.get('buscar')

    if busca:
        paciente = Paciente.objects.filter(nome_paciente__icontains=busca, profissional=request.user)
    else:
        paciente_list = Paciente.objects.filter(profissional=request.user)
        paginator = Paginator(paciente_list, 8)
        page = request.GET.get('page')
        paciente = paginator.get_page(page)

    return render(request, 'lista_pacientes.html', {'paciente': paciente})

@login_required(login_url='/login/')
def list_p_analise(request):
    busca = request.GET.get('buscar')

    if busca:
        paciente = Paciente.objects.filter(nome_paciente__icontains=busca, profissional=request.user)
    else:
        paciente_list = Paciente.objects.filter(profissional=request.user)
        paginator = Paginator(paciente_list, 8)
        page = request.GET.get('page')
        paciente = paginator.get_page(page)

    return render(request, 'lista_p_analise.html', {'paciente': paciente})


@login_required(login_url='/login/')
def list_consulta(request):

    busca = request.GET.get('buscar')

    if busca:
       consulta = Consulta.objects.filter(paciente__nome_paciente__icontains=busca, profissional=request.user)
    else:
        consulta_list = Consulta.objects.filter(profissional=request.user)
        paginator = Paginator(consulta_list, 8)
        page = request.GET.get('page')
        consulta = paginator.get_page(page)
    return render(request, 'lista_consultas.html', {'consulta': consulta})

@login_required(login_url='/login/')
def list_impressao(request, id):
    paciente = Paciente.objects.get(id=id)
    impressao = Impressao.objects.filter(paciente=paciente)

    return render(request, 'lista_impressoes.html', {'impressao': impressao, "paciente": paciente})

@login_required(login_url='/login/')
def list_im_analise(request,id):
    paciente = Paciente.objects.get(id=id)
    impressao = Impressao.objects.filter(paciente=paciente)

    return render(request, 'lista_impressao_ana.html', {'impressao': impressao, "paciente": paciente})

@login_required(login_url='/login/')
def pacientes_detalhes(request, id):
    paciente = Paciente.objects.get(id=id, profissional=request.user)

    return render(request, "detalhes_paciente.html", {'paciente': paciente})


@login_required(login_url='/login/')
def impressao_detalhes(request, id, id_impressao):
    impressao = Impressao.objects.get(id=id_impressao)
    return render(request, 'detalhes_impressoes.html', {'impressao': impressao})


@login_required(login_url='/login/')
def consulta_detalhes(request, id):
    consulta = Consulta.objects.get(id=id, profissional=request.user)
    return render(request, 'detalhes_consulta.html', {'consulta': consulta})


@login_required(login_url='/login/')
def inserir_digital(request, id):
    paciente = Paciente.objects.get(id=id)
    return render(request, 'inserir_digital.html', {'paciente': paciente})


@login_required(login_url='/login/')
def set_paciente(request):
    nome_paciente = request.POST.get('nome_paciente')
    cpf_paciente = request.POST.get('cpf_paciente')
    dt_nascimento = request.POST.get('dt_nascimento')
    file = request.FILES.get('file')
    id_paciente = request.POST.get('paciente-id')
    prof = request.user

    if id_paciente:
        paciente = Paciente.objects.get(id=id_paciente)
        if prof == paciente.profissional:
            paciente.nome_paciente = nome_paciente
            paciente.cpf_paciente = cpf_paciente
            paciente.dt_nascimento = dt_nascimento
            if file:
                paciente.foto = file
            paciente.save()
    elif Paciente.objects.filter(profissional=prof, cpf_paciente=cpf_paciente):
        messages.error(request, 'Paciente ja existe!')
        return redirect('../cadastrar_paciente/')

    else:

            paciente = Paciente.objects.create(foto=file, nome_paciente=nome_paciente, cpf_paciente=cpf_paciente,
                                           profissional=prof, dt_nascimento=dt_nascimento)
    messages.success(request, 'Paciente cadastrado com sucesso!')

    return redirect('../cadastrar_paciente/')


@login_required(login_url='/login/')
def delete_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    if paciente.profissional == request.user:
        paciente.delete()
    return redirect('../../pacientes/')


@login_required(login_url='/login/')
def delete_consulta(request, id):
    consulta = Consulta.objects.get(id=id)
    if consulta.profissional == request.user:
        consulta.delete()
    return redirect('../../consultas/')


@login_required(login_url='/login/')
def delete_impressao(request,id_impressao):
    impressao = Impressao.objects.get(id=id_impressao)
    impressao.delete()
    return redirect('../../../impressoes/', {'impressao': impressao})


@login_required(login_url='/login/')
def delete_impressao_a(request,id_impressao):
    id_impressao = Impressao.objects.get(id=id_impressao)
    id_impressao.delete()
    return redirect('../../impressoes_analise/')


@login_required(login_url='/login/')
def set_consulta(request,id):
    paciente = Paciente.objects.get(id=id)
    data = request.POST.get('data')
    horario = request.POST.get('horario')
    consulta_id = request.POST.get('consulta-id')
    prof = request.user

    if consulta_id:
        consulta = Consulta.objects.get(id=consulta_id)
        if prof == consulta.profissional:
            consulta.paciente = paciente
            consulta.data = data
            consulta.horario = horario
            consulta.save()

    elif Consulta.objects.filter(profissional=prof, horario=horario, data=data):
        messages.warning(request, 'Existe uma consulta marcada nesse horário e data. Por favor, tente novamente.')
        return redirect('../cadastrar_consulta/', {'paciente': paciente})

    else:

        Consulta.objects.create(data=data, paciente=paciente, profissional=prof, horario=horario)

    messages.success(request, 'Consulta Marcada!')

    return redirect('../cadastrar_consulta/', {'paciente': paciente})


@login_required(login_url='/login/')
def set_impressao(request, id):
    paciente = Paciente.objects.get(id=id)
    mao = request.POST.get('mao')
    dedo = request.POST.get('dedo')
    impressao_id = request.POST.get('impressao-id')
    file = request.FILES.get('file')
    contador = Impressao.objects.filter(paciente=paciente).count()
    if impressao_id:
        impressao = Impressao.objects.get(id=impressao_id)
        impressao.paciente = paciente
        impressao.mao = mao
        impressao.dedo = dedo

        if file:
            impressao.img = file
        impressao.save()

    else:

        impressao = Impressao.objects.create(mao=mao, dedo=dedo, paciente=paciente, img=file,cont=contador)

    contador +=1

    messages.success(request, 'Salvo com sucesso!')
    print('Contador:',contador)
    return redirect('../up_impressao/', {'paciente': paciente})

@login_required(login_url='/login/')
def atualizar_impressao(request, id):
    paciente = Paciente.objects.get(id=id)
    mao = request.POST.get('mao')
    dedo = request.POST.get('dedo')
    impressao_id = request.POST.get('impressao-id')
    file = request.FILES.get('file')
    contador = Impressao.objects.filter(paciente=paciente).count()
    if impressao_id:
        impressao = Impressao.objects.get(id=impressao_id)
        impressao.paciente = paciente
        impressao.mao = mao
        impressao.dedo = dedo

        if file:
            impressao.img = file
        impressao.save()

        # impressao = Impressao.objects.create(mao=mao, dedo=dedo, paciente=paciente, img=file,cont=contador)


    messages.success(request, 'Atualizado com sucesso!')
    print('Contador:',contador)
    return redirect('../impressoes_analise/', {'paciente': paciente})

@login_required(login_url='/login/')
def set_impressao_p(request, id):
    paciente = Paciente.objects.get(id=id)
    mao = request.POST.get('mao')
    dedo = request.POST.get('dedo')
    impressao_id = request.POST.get('impressao-id')
    file = request.FILES.get('file')
    contador = Impressao.objects.filter(paciente=paciente).count()
    if impressao_id:
        impressao = Impressao.objects.get(id=impressao_id)
        impressao.paciente = paciente
        impressao.mao = mao
        impressao.dedo = dedo

        if file:
            impressao.img = file
        impressao.save()

    else:

        impressao = Impressao.objects.create(mao=mao, dedo=dedo, paciente=paciente, img=file,cont=contador)

    contador +=1

    messages.success(request, 'Salvo com sucesso!')
    print('Contador:',contador)
    return render(request,'base_imp_m.html', {'paciente': paciente})

@csrf_protect
@login_required(login_url='/login/')
def form_consulta(request, id):
    id_paciente = Paciente.objects.get(id=id)
    consulta_id = request.GET.get('id')
    if consulta_id:
        consulta = Consulta.objects.get(id=consulta_id)

        if consulta.profissional == request.user:
            return render(request, 'base_consulta.html', {'consulta': consulta})

    return render(request, 'base_consulta.html', {'id_paciente': id_paciente})


@csrf_protect
@login_required(login_url='/login/')
def form_impressao(request, id):
    id_paciente = Paciente.objects.get(id=id)
    impressao_id = request.GET.get('id')
    if impressao_id:
        impressao = Impressao.objects.get(id=impressao_id)

        return render(request, 'base_impressao.html', {'impressao': impressao})

    return render(request, 'base_impressao.html', {'id_paciente': id_paciente})

@csrf_protect
@login_required(login_url='/login/')
def form_impressao_p(request, id):
    id_paciente = Paciente.objects.get(id=id)
    impressao_id = request.GET.get('id')
    if impressao_id:
        impressao = Impressao.objects.get(id=impressao_id)

        return render(request, 'base_imp_m.html', {'impressao': impressao})

    return render(request, 'base_imp_m.html', {'id_paciente': id_paciente})



@csrf_protect
@login_required(login_url='/login/')
def form_consulta_m(request):
    paciente = Paciente.objects.filter(profissional=request.user)
    id_paciente = request.GET.get("paciente")
    consulta_id = request.GET.get('id')
    if consulta_id:
        consulta = Consulta.objects.get(id=consulta_id)

        if consulta.profissional == request.user:
            return render(request, 'base_consulta_m.html', {'consulta': consulta})

    return render(request, 'base_consulta_m.html', {'id_paciente': id_paciente,'paciente':paciente})

@login_required(login_url='/login/')
def set_consulta_m(request):
    # id_paciente = Paciente.objects.get(id=id_paciente)
    paciente = request.POST.get("paciente")
    data = request.POST.get('data')
    horario = request.POST.get('horario')
    consulta_id = request.POST.get('consulta-id')
    prof = request.user

    if consulta_id:
        consulta = Consulta.objects.get(id=consulta_id)
        if prof == consulta.profissional:
            consulta.paciente = paciente
            consulta.data = data
            consulta.horario = horario
            consulta.save()

        if Consulta.objects.filter(profissional=prof, horario=horario, data=data):
            messages.warning(request, 'Existe uma consulta marcada nesse horário e data. Por favor, tente novamente.')
            return redirect('../cadastrar_consulta_m/', {'paciente': paciente})
    elif Consulta.objects.filter(profissional=prof, horario=horario, data=data) :
        messages.warning(request, 'Existe uma consulta marcada nesse horário e data. Por favor, tente novamente.')
        return redirect('../cadastrar_consulta_m/', {'paciente': paciente})

    else:

        Consulta.objects.create(data=data,horario=horario, paciente=paciente, profissional=prof )

    messages.success(request, 'Consulta Marcada!')

    return redirect('../cadastrar_consulta_m/',{'paciente':paciente})




