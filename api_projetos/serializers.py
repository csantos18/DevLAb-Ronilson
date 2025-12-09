from rest_framework import serializers
from .models import Projeto, ParticipacaoProjeto
from api_usuarios.models import Usuario
from api_usuarios.serializers import UsuarioSerializer
from api_equipes.models import Equipe
from api_equipes.serializers import EquipeSerializer

class ParticipacaoProjetoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), source='usuario', write_only=True
    )

    class Meta:
        model = ParticipacaoProjeto
        fields = ['id', 'usuario', 'usuario_id', 'papel', 'projeto']

class ProjetoSerializer(serializers.ModelSerializer):
    participantes = UsuarioSerializer(many=True, read_only=True)
    professor_responsavel = UsuarioSerializer(read_only=True)
    equipes = EquipeSerializer(many=True, read_only=True)  # traz todas as equipes relacionadas

    class Meta:
        model = Projeto
        fields = [
            'id',
            'titulo',
            'descricao',
            'cliente',
            'status',
            'data_inicio',
            'data_fim_prevista',
            'professor_responsavel',
            'participantes',
            'equipes'
        ]
