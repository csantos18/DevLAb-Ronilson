from django.contrib import admin
from django.urls import path
from api_usuarios import views as usuarios_views
from api_projetos import views as projetos_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login / Logout
    path('', usuarios_views.login_view, name='login'),
    path('logout/', usuarios_views.logout_view, name='logout'),

    # Home por tipo de usuário
    path('home/coordenador/', projetos_views.home_coordenador, name='home_coordenador'),
    path('home/professor/', projetos_views.home_professor, name='home_professor'),
    path('home/estudante/', projetos_views.home_estudante, name='home_estudante'),

    # PERFIL DO ESTUDANTE
    path('editar-perfil/', usuarios_views.editar_perfil, name='editar_perfil'),
    path('ver-perfil/', usuarios_views.ver_perfil, name='ver_perfil'),  # ✅ Corrigido: adicionada view ver_perfil

    # Criar Projeto / Equipe (somente coordenador)
    path('projetos/criar/', projetos_views.criar_projeto, name='criar_projeto'),
    path('equipes/criar/', projetos_views.criar_equipe, name='criar_equipe'),
]
