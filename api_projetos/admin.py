from django.contrib import admin
from .models import Projeto, Equipe


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'cliente',
        'status',
        'data_inicio',
        'data_fim_prevista',
        'professor_responsavel',
        'equipe',
    )
    list_filter = ('status',)
    search_fields = ('titulo', 'cliente')
    fields = (
        'titulo',
        'descricao',
        'cliente',
        'status',
        'data_inicio',
        'data_fim_prevista',
        'professor_responsavel',
        'equipe',
    )


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    
