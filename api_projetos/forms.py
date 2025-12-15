from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'cliente', 'status', 'professor_responsavel']  # adicione os campos do seu model
