from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Equipe, ParticipacaoEquipe
from api_projetos.models import Projeto
from api_usuarios.models import Usuario

# Criar equipe
@login_required
def criar_equipe(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        projeto_id = request.POST['projeto']
        lider_id = request.POST['lider']
        projeto = get_object_or_404(Projeto, id=projeto_id)
        lider = get_object_or_404(Usuario, id=lider_id)
        Equipe.objects.create(nome=nome, descricao=descricao, projeto=projeto, lider=lider)
        return redirect('home_coordenador')
    
    projetos = Projeto.objects.all()
    lideres = Usuario.objects.filter(tipo='estudante')
    return render(request, 'criar_equipe.html', {'projetos': projetos, 'lideres': lideres})

# Detalhe equipe
@login_required
def detalhe_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    participacoes = ParticipacaoEquipe.objects.filter(equipe=equipe)
    return render(request, 'detalhe_equipe.html', {'equipe': equipe, 'participacoes': participacoes})
