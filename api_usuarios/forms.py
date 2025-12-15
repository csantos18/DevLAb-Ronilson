from django import forms
from .models import Usuario
from api_projetos.models import Equipe


# Form para editar perfil
class EditarPerfilForm(forms.ModelForm):
    senha_nova = forms.CharField(
        label='Nova Senha',
        widget=forms.PasswordInput,
        required=False,
        help_text='Deixe em branco se não quiser alterar a senha.'
    )

    class Meta:
        model = Usuario
        fields = ['email']  

    def save(self, commit=True):
        usuario = super().save(commit=False)
        senha = self.cleaned_data.get('senha_nova')
        if senha:
            usuario.set_password(senha)
        if commit:
            usuario.save()
        return usuario


# Form para criar equipe
class CriarEquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'descricao', 'membros']
