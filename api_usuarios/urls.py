from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_usuarios'  # ESSENCIAL para namespace

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    # -------- APIs --------
    path(
        'usuarios_filtrados/<str:tipo>/',
        views.usuarios_filtrados,
        name='usuarios_filtrados'
    ),

    # -------- ESTUDANTE --------
    path(
        'home/estudante/',
        views.home_estudante,
        name='home_estudante'
    ),

    path(
        'editar_perfil/',
        views.editar_perfil,
        name='editar_perfil'
    ),

    path(
        'ver_perfil/',
        views.ver_perfil,
        name='ver_perfil'
    ),

    path(
        'lista_projetos/',
        views.lista_projetos,
        name='lista_projetos'
    ),

    # -------- EQUIPES --------
    path(
        'criar_equipe/<int:projeto_id>/',
        views.criar_equipe,
        name='criar_equipe'
    ),

    # -------- DRF --------
    path('', include(router.urls)),
]
