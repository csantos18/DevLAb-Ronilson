from django.contrib.auth.models import AbstractUser
from django.db import models

TIPOS_USUARIO = (
    ('coordenador', 'Coordenador'),
    ('professor', 'Professor'),
    ('estudante', 'Estudante'),
)

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS_USUARIO)

    REQUIRED_FIELDS = ['email', 'matricula']
    
    def __str__(self):
        return self.username
