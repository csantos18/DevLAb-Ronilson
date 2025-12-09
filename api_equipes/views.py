from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Equipe
from .serializers import EquipeSerializer
from .permissions import IsProfessorOrCoordenador  # type: ignore

# POST /equipes/criar
class CriarEquipeView(generics.CreateAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [IsAuthenticated, IsProfessorOrCoordenador]

# DELETE /equipes/deletar/<id>
class DeletarEquipeView(generics.DestroyAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [IsAuthenticated, IsProfessorOrCoordenador]
    lookup_url_kwarg = "id_equipe"

# GET /equipes/listar
class ListarEquipesView(generics.ListAPIView):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [IsAuthenticated]
