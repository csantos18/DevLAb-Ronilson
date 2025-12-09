from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    path('usuarios_filtrados/<str:tipo>/', views.usuarios_filtrados, name='usuarios_filtrados'),
    path('', include(router.urls)),
]
