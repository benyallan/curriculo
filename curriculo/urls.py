from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import DadosPessoaisViewSet, TelefoneViewSet
from portifolio.api.viewsets import PortifolioViewSet
from experienciaProfissional.api.viewsets import ExperienciaProfissionalViewSet
from formacao.api.viewsets import FormacaoViewSet
from cursos.api.viewsets import CursoViewSet
from idiomas.api.viewsets import IdiomaViewSet
from habilidades.api.viewsets import HabilidadeViewSet
from .views import welcome


router = routers.DefaultRouter()
router.register(r'dadospessoais', DadosPessoaisViewSet)
router.register(r'telefones', TelefoneViewSet)
router.register(r'portifolio', PortifolioViewSet)
router.register(r'experienciaprofissional', ExperienciaProfissionalViewSet)
router.register(r'formacao', FormacaoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'idiomas', IdiomaViewSet)
router.register(r'habilidades', HabilidadeViewSet)


urlpatterns = [
    path('', welcome),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
