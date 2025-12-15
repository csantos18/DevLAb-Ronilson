from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Projeto, Equipe, ParticipacaoEquipe
from .forms import ProjetoForm
from api_usuarios.forms import CriarEquipeForm


# =========================
# HOME COORDENADOR
# =========================
@login_required
def home_coordenador(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    projetos = Projeto.objects.all()
    equipes = Equipe.objects.all()

    return render(
        request,
        'home_coordenador.html',
        {
            'projetos': projetos,
            'equipes': equipes
        }
    )


# =========================
# CRIAR PROJETO
# =========================
@login_required
def criar_projeto(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_coordenador')
    else:
        form = ProjetoForm()

    return render(request, 'criar_projeto.html', {'form': form})


# =========================
# CRIAR EQUIPE
# =========================
@login_required
def criar_equipe(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    if request.method == 'POST':
        form = CriarEquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_coordenador')
    else:
        form = CriarEquipeForm()

    return render(request, 'criar_equipe.html', {'form': form})


# =========================
# HOME PROFESSOR
# =========================
@login_required
def home_professor(request):
    if request.user.tipo != 'professor':
        return redirect('login')

    projetos = Projeto.objects.filter(professor_responsavel=request.user)
    equipes = Equipe.objects.filter(projetos__in=projetos).distinct()

    return render(
        request,
        'home_professor.html',
        {
            'projetos': projetos,
            'equipes': equipes
        }
    )


# =========================
# HOME ESTUDANTE
# =========================
@login_required
def home_estudante(request):
    if request.user.tipo != 'estudante':
        return redirect('login')

    participacoes_equipes = ParticipacaoEquipe.objects.filter(usuario=request.user)
    equipes = Equipe.objects.filter(
        participacaoequipe__in=participacoes_equipes
    ).distinct()

    projetos = Projeto.objects.filter(equipe__in=equipes).distinct()

    return render(
        request,
        'home_estudante.html',
        {
            'projetos': projetos,
            'equipes': equipes
        }
    )
