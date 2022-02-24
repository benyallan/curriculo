from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import DadosPessoaisViewSet
from portifolio.api.viewsets import PortifolioViewSet
from experienciaProfissional.api.viewsets import ExperienciaProfissionalViewSet
from formacao.api.viewsets import FormacaoViewSet
from cursos.api.viewsets import CursoViewSet


router = routers.DefaultRouter()
router.register(r'dadospessoais', DadosPessoaisViewSet)
router.register(r'portifolio', PortifolioViewSet)
router.register(r'experienciaprofissional', ExperienciaProfissionalViewSet)
router.register(r'formacao', FormacaoViewSet)
router.register(r'cursos', CursoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
