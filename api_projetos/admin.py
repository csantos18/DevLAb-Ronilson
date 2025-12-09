from django.contrib import admin
from .models import Projeto, ParticipacaoProjeto
from api_equipes.models import Equipe

class ParticipacaoProjetoInline(admin.TabularInline):
    model = ParticipacaoProjeto
    extra = 0
    readonly_fields = ('usuario', 'papel')
    can_delete = False

class EquipeInline(admin.TabularInline):
    model = Equipe
    extra = 0
    readonly_fields = ('nome', 'descricao', 'lider')
    can_delete = False

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'status', 'data_inicio', 'data_fim_prevista', 'professor_responsavel')
    list_filter = ('status',)
    search_fields = ('titulo', 'cliente')
    fields = ('titulo', 'descricao', 'cliente', 'status', 'data_inicio', 'data_fim_prevista', 'professor_responsavel')

    inlines = [ParticipacaoProjetoInline, EquipeInline]  # mostra alunos e equipes na página do projeto

@admin.register(ParticipacaoProjeto)
class ParticipacaoProjetoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'projeto', 'papel')
