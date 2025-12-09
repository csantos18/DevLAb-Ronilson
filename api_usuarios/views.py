from rest_framework import viewsets, permissions
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .serializers import UsuarioSerializer

# ---------------- PERMISSÕES ----------------
class IsCoordenador(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'coordenador'

class IsProfessor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'professor'

# ---------------- VIEWSET USUÁRIOS ----------------
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        user = self.request.user
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if user.tipo == 'coordenador' or user.tipo == 'professor':
                return [permissions.IsAuthenticated()]
            else:
                return [permissions.IsAdminUser()]  # estudante não pode alterar
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.tipo == 'estudante':
            return Usuario.objects.filter(id=user.id)
        elif user.tipo == 'professor':
            return Usuario.objects.filter(tipo='estudante')
        return Usuario.objects.all()

# ---------------- FILTRAR USUÁRIOS ----------------
@login_required
def usuarios_filtrados(request, tipo):
    """
    Filtra usuários por tipo: 'estudante', 'professor' ou 'coordenador'
    """
    usuarios = Usuario.objects.filter(tipo=tipo)
    return render(request, 'usuarios_filtrados.html', {'usuarios': usuarios, 'tipo': tipo})
