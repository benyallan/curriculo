from experienciaProfissional.models import ExperienciaProfissional
from .serializers import ExperienciaProfissionalSerializer
from rest_framework import viewsets


class ExperienciaProfissionalViewSet(viewsets.ModelViewSet):
    queryset = ExperienciaProfissional.objects.all()
    serializer_class = ExperienciaProfissionalSerializer