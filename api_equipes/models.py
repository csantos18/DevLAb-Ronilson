from django.db import models
from api_projetos.models import Projeto
from api_usuarios.models import Usuario

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    lider = models.ForeignKey(
        Usuario, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='equipes_lideradas'
    )
    projeto = models.ForeignKey(
        Projeto, 
        on_delete=models.CASCADE, 
        related_name='equipes'
    )

    def __str__(self):
        return self.nome

class ParticipacaoEquipe(models.Model):
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='participacoes_equipes'
    )
    equipe = models.ForeignKey(
        Equipe, 
        on_delete=models.CASCADE, 
        related_name='participacoes'
    )
    data_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.equipe.nome}"
