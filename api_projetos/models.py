from django.db import models
from api_usuarios.models import Usuario


class Equipe(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)

    membros = models.ManyToManyField(
        Usuario,
        through='ParticipacaoEquipe',
        related_name='equipes'
    )

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    cliente = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='Em andamento')
    data_inicio = models.DateField()
    data_fim_prevista = models.DateField()

    professor_responsavel = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projetos'
    )

    equipe = models.ForeignKey(
        Equipe,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projetos'
    )

    def __str__(self):
        return self.titulo


class ParticipacaoEquipe(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    papel = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.usuario.username} - {self.equipe.nome}"
