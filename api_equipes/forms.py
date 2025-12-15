from django import forms
from .models import Equipe

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'descricao', 'lider', 'projeto']  # campos do seu model
