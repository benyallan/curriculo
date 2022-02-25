from .serializers import HabilidadeSerializer
from habilidades.models import Habilidade
from rest_framework import viewsets


class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer