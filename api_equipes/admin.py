from django.contrib import admin
from .models import Equipe

class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'projeto', 'lider']

admin.site.register(Equipe, EquipeAdmin)
