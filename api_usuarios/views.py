from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario:
            login(request, usuario)

            # Redireciona de acordo com o tipo
            if usuario.tipo == 'coordenador':
                return redirect('home_coordenador')
            elif usuario.tipo == 'professor':
                return redirect('home_professor')
            elif usuario.tipo == 'estudante':
                return redirect('home_estudante')
            else:
                messages.error(request, "Tipo de usuário inválido.")
                logout(request)
                return redirect('login')
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ----------------------------
# View para editar perfil
# ----------------------------
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('home_estudante')
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'editar_perfil.html', {'form': form})


# ----------------------------
# View para VER PERFIL (nº 3)
# ----------------------------
@login_required
def ver_perfil(request):
    return render(request, 'ver_perfil.html', {
        'usuario': request.user
    })
