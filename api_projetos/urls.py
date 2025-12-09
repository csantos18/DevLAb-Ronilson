from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjetoViewSet,
    ParticipacaoProjetoViewSet,
    lista_projetos,
    lista_equipes
)

router = DefaultRouter()
router.register(r'projetos', ProjetoViewSet)
router.register(r'participacoes', ParticipacaoProjetoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lista/', lista_projetos, name='lista_projetos'),
    path('equipes/', lista_equipes, name='lista_equipes'),
]
